import os, argparse, inflect, xml.etree.ElementTree as etree

engine = inflect.engine()

PRIMARY_KEY_LABEL = 'primary'
XML_NAMESPACE = '{http://www.w3.org/2001/XMLSchema-instance}'

MODEL_SNIPPET =  os.path.join('snippets', 'Model.php')
RESOURCE_MODEL_SNIPPET = os.path.join('snippets', 'ResourceModel.php')
COLLECTION_SNIPPET = os.path.join('snippets', 'Collection.php')

OUTPUT_DIR = os.path.relpath('output')
MODEL_DIR = os.path.join(OUTPUT_DIR, 'Models')
RESOURCE_MODEL_DIR = os.path.join(MODEL_DIR, 'ResourceModel')

def mass_replace(string, **kwargs):
    for key, value in kwargs.items(): string = string.replace('[{}]'.format(key), value)
    return string

def fill_snippet(input_path, output_path, parse_line_function):
    with open(input_path) as filein:
        with open(output_path, 'w+') as fileout:
            for line in filein:
                fileout.write(parse_line_function(line))

def generate_class(input_path, output_path, **kwargs):
    for directory in os.path.split(output_path)[:-1]:
        if not os.path.exists(directory):
            os.mkdir()

    fill_snippet(input_path, output_path, lambda line: mass_replace(line, **kwargs))

def snake_to_pascal(snake_str):
    words = map(lambda word: word.capitalize(), snake_str.split('_'))
    return ''.join(words)

for directory in [OUTPUT_DIR, MODEL_DIR, RESOURCE_MODEL_DIR]:
    if not os.path.exists(directory): os.mkdir(directory)

parser = argparse.ArgumentParser(description='Generate all the files')
parser.add_argument('schema', type=str, help='Input file')

args = parser.parse_args()

tree = etree.parse(args.schema)
root = tree.getroot()

for table in root.findall('table'):
    table_name = table.get('name')
    primary_key = ''
    
    for constraint in table.findall('constraint'):
        if constraint.get(XML_NAMESPACE + 'type') == PRIMARY_KEY_LABEL:
            primary_key = constraint.find('column').get('name')

    model_class = engine.singular_noun(snake_to_pascal(table_name))
    # TODO: add option for class shortening (namespaces)

    generate_class(RESOURCE_MODEL_SNIPPET, os.path.join(RESOURCE_MODEL_DIR, model_class + '.php'), 
        model = model_class, table = table_name, primary_key = primary_key)
    generate_class(MODEL_SNIPPET, os.path.join(MODEL_DIR, model_class + '.php'), 
        model = model_class, resource_model = model_class)
    
    collection_directory = os.path.join(RESOURCE_MODEL_DIR, model_class)
    if not os.path.exists(collection_directory):
        os.mkdir(collection_directory)
    generate_class(COLLECTION_SNIPPET, os.path.join(RESOURCE_MODEL_DIR, model_class, 'Collection.php'), 
        model = model_class, resource_model = model_class, primary_key = primary_key)