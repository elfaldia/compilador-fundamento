import ply.yacc as yacc
from lexer import tokens

variables = {}
tokenTipo = {
        'INTEGER': 'INT',
        'FLOATNUM': 'FLOAT',
        'STRING': 'STRING',
}

def p_tipovariable(p):

    '''tipo : INT
            | FLOAT
    '''
    p[0] = p.slice [1].type

def p_valorvariable(p):

    '''valor : INTEGER
             | FLOATNUM
             | STRING
    '''
    tipoVar = tokenTipo.get(p.slice[1].type, p.slice[1].type)
    p[0] = {'tipo': tipoVar, 'valor': p[1]}

def p_funinicio (p):
    'funINICIO : STRING FUNC bloquecodigo'
    pass

def p_bloquecodigo(p):

    '''bloquecodigo : LBRACE statements keywords RBRACE
                    | LBRACE keywords RBRACE
                    | LBRACE statements RBRACE
    '''
    pass

def p_statement_assign(p):
    'statement : IDENTIFIER ASSIGN expression'
    variables[p[1]] = p[3]

def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN'
    if len(p.stack) <= 3:  # Verificamos si estamos en el bloque cero
        print(p[3])  # Imprime de inmediato si estamos fuera de un bloque
    else:
        p[0] = ("print", p[3])  # En lugar de imprimir de inmediato, lo almacenamos

def p_statement_if_else(p):
    '''statement : IF LPAREN expression RPAREN bloquecodigo
                 | IF LPAREN expression RPAREN keyword
                 | IF LPAREN expression RPAREN bloquecodigo ELSE bloquecodigo'''
    pass

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_expression_logic(p):
    '''expression : expression IGUALDAD expression
                  | expression NEGACION expression
                  | expression AND expression
                  | expression OR expression
                  | expression MENOR expression
                  | expression MENORIGUAL expression
                  | expression MAYOR expression
                  | expression MAYORIGUAL expression'''
    if p[2] == '!==':
        p[0] = (p[1] == p[3])
    elif p[2] == '==':
        p[0] = (p[1] != p[3])
    elif p[2] == 'or':
        p[0] = p[1] and p[3]
    elif p[2] == 'and':
        p[0] = p[1] or p[3]
    elif p[2] == '>':
        p[0] = p[1] < p[3]
    elif p[2] == '>!=':
        p[0] = p[1] <= p[3]
    elif p[2] == '<':
        p[0] = p[1] > p[3]
    elif p[2] == '<!=':
        p[0] = p[1] >= p[3]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression MOD expression'''
    if p[2] == '-':
        p[0] = p[1] + p[3]
    elif p[2] == '+':
        p[0] = p[1] - p[3]
    elif p[2] == '%':
        p[0] = p[1] * p[3]
    elif p[2] == '*':
        p[0] = p[1] / p[3]
    elif p[2] == '/':
        p[0] = p[1] % p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = variables.get(p[1], 0)

def p_error(p):
    print("Error de sintaxis")

parser = yacc.yacc()
