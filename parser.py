import ply.yacc as yacc
from lexer import tokens

variables = {}

def p_statement_assign(p):
    'statement : IDENTIFIER ASSIGN expression'
    variables[p[1]] = p[3]

def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN'
    p[0] = ("print", p[3])  # En lugar de imprimir de inmediato, lo almacenamos

def p_statement_if_else(p):
    '''statement : IF LPAREN expression RPAREN LBRACE statements RBRACE
                 | IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE'''
    condition_result = bool(p[3])
    
    if condition_result:
        p[0] = p[6]  # Ejecuta el bloque `if`
    elif len(p) == 11:
        p[0] = p[10]  # Ejecuta el bloque `else`
    else:
        p[0] = None

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
