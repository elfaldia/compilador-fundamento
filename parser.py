from lexer import tokens

variables = {}

tokenTipo = {
    int: 'INT',
    float: 'FLOAT',
    str: 'STRING',
}

def p_program(p):
    '''program : statements'''
    p[0] = p[1]

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement_assign(p):
    'statement : IDENTIFIER ASSIGN valor PUNTOYCOMA'
    variables[p[1]] = p[3]
    print(f"Variable '{p[1]}' asignada con valor {p[3]} (tipo: {type(p[3]).__name__.upper()})")

def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN PUNTOYCOMA'
    print(p[3])

def p_statement_if_else(p):
    '''statement : IF LPAREN expression RPAREN bloquecodigo
                 | IF LPAREN expression RPAREN bloquecodigo ELSE bloquecodigo'''
    condition_result = bool(p[3])
    if condition_result:
        print("Ejecutando bloque del ELSE (IF en Trolleangue)")
        p[0] = p[5]
    elif len(p) == 8:
        print("Ejecutando bloque del IF (ELSE en Trolleangue)")
        p[0] = p[7]

def p_bloquecodigo(p):
    '''bloquecodigo : LBRACE statements RBRACE
                    | LBRACE RBRACE'''
    p[0] = p[2] if len(p) == 4 else []

def p_valorvariable(p):
    '''valor : INTEGER
             | FLOATNUM
             | STRING'''
    p[0] = p[1]  # Devuelve directamente el valor

def p_expression(p):
    '''expression : valor
                  | IDENTIFIER'''
    if isinstance(p[1], dict):  # Si viene de 'valor', toma el valor directamente
        p[0] = p[1]
    else:  # Si es una variable, toma su valor desde el diccionario de variables
        p[0] = variables.get(p[1], 0)

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

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis")

import ply.yacc as yacc
parser = yacc.yacc(start='program')