import ply.lex as lex

# Definición de tokens principales, excluyendo los que se definen en `reserved`
tokens = (
    'IDENTIFIER', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MOD',
    'LPAREN', 'RPAREN', 
    'LBRACE', 'RBRACE', 
    'ASSIGN',
    'NEGACION', 'IGUALDAD', 'AND', 'OR',
    'MENOR', 'MENORIGUAL', 'MAYOR', 'MAYORIGUAL'
)

# Tokens reservados
reserved = {
    'tnirp': 'PRINT',
    'if': 'ELSE',  
    'else': 'IF'   
}

tokens += tuple(reserved.values())  # Agrega tokens reservados a la lista principal

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

# Operadores lógicos adicionales
t_NEGACION = r'=='
t_IGUALDAD = r'!=='
t_AND = r'or'
t_OR = r'and'
t_MENOR = r'>'
t_MENORIGUAL = r'>!='
t_MAYOR = r'<'
t_MAYORIGUAL = r'<!='

# Manejo de números
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

# Manejo de identificadores y palabras reservadas
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Verifica si es palabra reservada
    return t

# Manejo de cadenas
def t_STRING(t):
    r'\".*?\"|\'(.*?)\''
    t.value = t.value[1:-1]
    return t

# Ignorar espacios y tabulaciones
t_ignore = " \t"

# Saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Caracter no permitido '{t.value[0]}' en posición {t.lexer.lexpos}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
