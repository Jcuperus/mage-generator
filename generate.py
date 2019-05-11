import os, argparse, inflect, xml.etree.ElementTree as etree

engine = inflect.engine()

PRIMARY_KEY_LABEL = 'primary'
XML_NAMESPACE = '{http://www.w3.org/2001/XMLSchema-instance}'

OUTPUT_DIR = 'output'
MODEL_DIR = OUTPUT_DIR + '/Models'
RESOURCE_MODEL_DIR = MODEL_DIR + '/ResourceModel'

def snake_to_pascal(snake_str):
    words = snake_str.split('_')
    output = ''
    for word in words:
        output += word.capitalize()
    return output

if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)

if not os.path.exists(RESOURCE_MODEL_DIR):
    os.mkdir(RESOURCE_MODEL_DIR)

parser = argparse.ArgumentParser(description='Generate all the files')
parser.add_argument('schema', type=str, help='Input file')

args = parser.parse_args()

tree = etree.parse(args.schema)
root = tree.getroot()

for table in root.findall('table'):
    tablename = table.get('name')
    primary_key = ''
    
    for constraint in table.findall('constraint'):
        if constraint.get(XML_NAMESPACE + 'type') == PRIMARY_KEY_LABEL:
            primary_key = constraint.find('column').get('name')

    model_class = engine.singular_noun(snake_to_pascal(tablename))

    with open('snippets/ResourceModel.php') as filein:
        with open(RESOURCE_MODEL_DIR + '/' + model_class + '.php', 'w+') as fileout:
            for line in filein:
                lineout = line.replace('{model}', model_class).replace('{table}', tablename).replace('{primary_key}', primary_key)
                fileout.write(lineout)

    with open('snippets/Model.php') as filein:
        with open(MODEL_DIR + '/' + model_class + '.php', 'w+') as fileout:
            for line in filein:
                fileout.write(line.replace('{model}', model_class))

    with open('snippets/Collection.php') as filein:
        if not os.path.exists(RESOURCE_MODEL_DIR + '/' + model_class):
            os.mkdir(RESOURCE_MODEL_DIR + '/' + model_class)
        with open(RESOURCE_MODEL_DIR + '/' + model_class + '/Collection.php', 'w+') as fileout:
            for line in filein:
                lineout = line.replace('{model}', model_class).replace('{primary_key}', primary_key)
                fileout.write(lineout)