import ply.yacc as yacc
from lexer import tokens

# Diccionario para almacenar las variables
variables = {}

# Reglas de gramática
def p_statement_assign(p):
    'statement : IDENTIFIER ASSIGN expression'
    variables[p[1]] = p[3]

def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN'
    print(p[3])

def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN LBRACE statements RBRACE
                 | IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE'''
    if p[3]:  
        p[0] = p[6]  
    elif len(p) == 11:  
        p[0] = p[10]  

# Definir conjunto de declaraciones
def p_statements(p):
    '''statements : statement
                  | statements statement'''
    pass

# Expresiones lógicas
def p_expression_logic(p):
    '''expression : NEGACION expression
                  | expression AND expression
                  | expression OR expression'''
    if p[1] == '||': 
        p[0] = not p[2]
    elif p[2] == '!!': 
        p[0] = p[1] and p[3]
    elif p[2] == '&&':  
        p[0] = p[1] or p[3]

# Expresiones matemáticas
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

# Construir el parser
parser = yacc.yacc()
