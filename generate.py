import os, argparse
from xml.etree import ElementTree
from jinja2 import Environment, PackageLoader
from textformat import snake_to_pascal, snake_to_camel, singular, translate_sql_type

env = Environment(loader=PackageLoader('generate', 'templates'))

MODEL_TEMPLATE = env.get_template('Model.php')
RESOURCEMODEL_TEMPLATE = env.get_template('ResourceModel.php')
COLLECTION_TEMPLATE = env.get_template('Collection.php')
DATA_INTERFACE_TEMPLATE = env.get_template('DataInterface.php')

parser = argparse.ArgumentParser(description='Generate all the files')
parser.add_argument('schema', type=str, help='Input file')
parser.add_argument('-n', '--namespace', type=str, help='Class namespace')
parser.add_argument('-o', '--output', type=str, help='Output path')
args = parser.parse_args()

namespace = args.namespace if args.namespace else ''

PRIMARY_KEY_LABEL = 'primary'
XML_NAMESPACE = '{http://www.w3.org/2001/XMLSchema-instance}'

OUTPUT_DIR = os.path.relpath(args.output) if args.output else os.path.relpath('output')
API_DIR = os.path.join(OUTPUT_DIR, 'Api')
API_DATA_DIR = os.path.join(API_DIR, 'Data')
MODEL_DIR = os.path.join(OUTPUT_DIR, 'Models')
RESOURCE_MODEL_DIR = os.path.join(MODEL_DIR, 'ResourceModel')

def generate_file(path, template, **kwargs):
    with open(path, 'w+') as fileout:
        fileout.write(template.render(*kwargs))

for directory in [OUTPUT_DIR, API_DIR, API_DATA_DIR, MODEL_DIR, RESOURCE_MODEL_DIR]:
    if not os.path.exists(directory): os.mkdir(directory)

tree = ElementTree.parse(args.schema)
root = tree.getroot()

for table in root.findall('table'):
    table_name = table.get('name')
    columns = []
    primary_key = ''
    
    for constraint in table.findall('constraint'):
        if constraint.get(XML_NAMESPACE + 'type') == PRIMARY_KEY_LABEL:
            primary_key = constraint.find('column').get('name')

    for column in table.findall('column'):
        columns.append({
            'name': column.get('name'), 
            'type': translate_sql_type(column.get(XML_NAMESPACE + 'type')),
            'pascal': snake_to_pascal(column.get('name')),
            'camel': snake_to_camel(column.get('name'))
        })

    model_class = singular(snake_to_pascal(table_name))
    if model_class != namespace: model_class = model_class.replace(namespace, '')
    
    generate_file(os.path.join(RESOURCE_MODEL_DIR, model_class + '.php'), RESOURCEMODEL_TEMPLATE,
        model=model_class, table=table_name, primary_key=primary_key)
    
    generate_file(os.path.join(MODEL_DIR, model_class + '.php'), MODEL_TEMPLATE,
        model=model_class, resource_model=model_class, columns=columns)

    if not os.path.exists(os.path.join(RESOURCE_MODEL_DIR, model_class)): 
        os.mkdir(os.path.join(RESOURCE_MODEL_DIR, model_class))
    
    generate_file(os.path.join(RESOURCE_MODEL_DIR, model_class, 'Collection.php'), COLLECTION_TEMPLATE,
        model=model_class, resource_model=model_class, primary_key=primary_key)

    generate_file(os.path.join(API_DATA_DIR, model_class + 'Interface.php'), DATA_INTERFACE_TEMPLATE,
        model=model_class, columns=columns)