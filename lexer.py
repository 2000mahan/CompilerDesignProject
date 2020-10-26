from ply import lex

class lexer:

    tokens = {
       'ID', 'INTEGERNUMBER', 'FLOATNUMBER', 'INTEGER', 'FLOAT',
        'BOOLEAN', 'FUNCTION', 'TRUE', 'FALSE', 'PRINT', 'RETURN',
        'MAIN', 'IF', 'ELSE', 'ELSEIF', 'WHILE', 'ON', 'WHERE', 'FOR',
        'AND', 'OR', 'NOT', 'IN', 'ASSIGN', 'SUM', 'SUB', 'MUL', 'DIV',
        'MOD', 'GT', 'GE', 'LT', 'LE', 'EQ', 'NE', 'LCB', 'RCB',
        'LRB', 'RRB', 'LSB', 'RSB', 'SEMICOLON', 'COLON', 'COMMA', 'ERROR!'
    }
    # COLONS
    t_SEMICOLON = r';'
    t_COLON = r':'
    t_COLON = r'COMMA'
    # OPERATORS
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_ASSIGN = r'='
    t_LT = r'\<'
    t_GT = r'\>'
    # BRACKETS
    t_LCB = r'\{'
    t_RCB = r'\}'
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LSB = r'\[>'
    t_RSB = r'\]>'


