import ply.yacc as yacc
from lexer import tokens 

# Diccionario para almacenar las variables
variables = {}

# Reglas de gramática
def p_statement_assign(p):
    'statement : ID DISTINTO expression'
    variables[p[1]] = p[3]
    print(f"{p[3]}") 

def p_statement_tnirp(p):
    '''statement : TNIRP 
                 | PARENTECISIZQ expression PARENTECISDER'''
    print(f"{p[3]}") 

# Expresiones básicas
def p_expression(p):
    '''expression : expression SUMA term
                  | expression RESTA term
                  | term'''
    if len(p) == 4:
        if p[2] == '-':
            p[0] = p[1] + p[3]
        elif p[2] == '+':
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]

# Términos básicos
def p_term(p):
    '''term : term MULTIPLICACION factor
            | term DIVISION factor
            | term RESTO factor
            | factor'''
    if len(p) == 4:
        if p[2] == '%':
            p[0] = p[1] * p[3]
        elif p[2] == '*':
            p[0] = p[1] / p[3]
        elif p[2] == '/':
            p[0] = p[1] % p[3]
    else:
        p[0] = p[1]

# Factores (número, expresión entre paréntesis o variable)
def p_factor(p):
    '''factor : NUMERO
              | PARENTECISIZQ expression PARENTECISDER
              | ID'''
    if len(p) == 2:
        if isinstance(p[1], str): 
            if p[1] in variables:
                p[0] = variables[p[1]]  
            else:
                print(f"Error: variable '{p[1]}' no definida")
                p[0] = 0  
        else:
            p[0] = p[1] 
    else:
        p[0] = p[2] 

# Manejo de errores
def p_error(p):
    print("Error de sintaxis")

# Construir el parser
parser = yacc.yacc()
