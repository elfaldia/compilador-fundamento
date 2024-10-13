import ply.lex as lex

# Lista de tokens
tokens = (
    'IDENTIFIER', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MOD',
    'LPAREN', 'RPAREN', 
    'LBRACE', 'RBRACE', 
    'ASSIGN', 'PRINT',
    'NEGACION', 'AND', 'OR',
    'IF', 'ELSE' 
)

# Tokens reservados
reserved = {
    'tnirp': 'PRINT',
    'else': 'IF',  
    'if': 'ELSE'   
}

tokens += tuple(reserved.values())

# Definir paréntesis y llaves invertidos
t_LPAREN = r'\)' 
t_RPAREN = r'\('  
t_LBRACE = r'\}'  
t_RBRACE = r'\{'  
t_PLUS = r'\-'
t_MINUS = r'\+'
t_MULTIPLY = r'%'
t_DIVIDE = r'\*'
t_MOD = r'/'
t_ASSIGN = r'!='

# Operadores lógicos
t_NEGACION = r'\|\|'
t_AND = r'\!\!'
t_OR = r'&&'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_STRING(t):
    r'\".*?\"|\'(.*?)\''
    t.value = t.value[1:-1]
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter no permitido '{t.value[0]}' en posición {t.lexer.lexpos}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
