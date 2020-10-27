from ply import lex

class lexer:

    tokens = [
       'ID', 'INTEGERNUMBER', 'FLOATNUMBER', 'INTEGER', 'FLOAT',
        'BOOLEAN', 'FUNCTION', 'TRUE', 'FALSE', 'PRINT', 'RETURN',
        'MAIN', 'IF', 'ELSE', 'ELSEIF', 'WHILE', 'ON', 'WHERE', 'FOR',
        'AND', 'OR', 'NOT', 'IN', 'ASSIGN', 'SUM', 'SUB', 'MUL', 'DIV',
        'MOD', 'GT', 'GE', 'LT', 'LE', 'EQ', 'NE', 'LCB', 'RCB',
        'LRB', 'RRB', 'LSB', 'RSB', 'SEMICOLON', 'COLON', 'COMMA', 'ERROR!'
    ]
    reserved = {
        # Conditional
        'if': 'IF',
        'then': 'THEN',
        'else': 'ELSE',
        'elseif': 'ELSEIF',
        # Loops
        'for': 'FOR',
        'while': 'WHILE',
        # Types
        'int': 'INTEGER',
        'float': 'FLOAT',
        'bool': 'BOOLEAN',
        # Other Keywords
        'print': 'PRINT',
        'true': 'TRUE',
        'false': 'FALSE',
        'return': 'RETURN',
        'fun': 'FUNCTION',
        'main': 'MAIN',
        'on': 'ON',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
        'in': 'IN',
    }
    # Colons
    t_SEMICOLON = r';'
    t_COLON = r':'
    t_COLON = r'COMMA'
    # Operators
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_ASSIGN = r'='
    t_LT = r'\<'
    t_GT = r'\>'
    # Brackets
    t_LCB = r'\{'
    t_RCB = r'\}'
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LSB = r'\[>'
    t_RSB = r'\]>'


