import inflect

engine = inflect.engine()

TYPE_CONVERSIONS = {
    'varchar': 'string',
    'smallint': 'int',
    'decimal': 'int'
}

def singular(string):
    return engine.singular_noun(string)    

def snake_to_pascal(string):
    return ''.join(map(lambda word: word.capitalize(), string.split('_')))

def snake_to_camel(string):
    words = string.split('_')
    return words[0] + ''.join(map(lambda word: word.capitalize(), words[1:]))

def translate_sql_type(type):
    return TYPE_CONVERSIONS[type] if type in TYPE_CONVERSIONS.keys() else type