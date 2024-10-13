from lexer import lexer  # Importa el lexer
from parser import parser  # Importa el parser

# Función principal
def main():
    while True:
        try:
            s = input('Trolleangue > ') 
        except EOFError:
            break
        if not s.strip():  
            continue
        result = parser.parse(s)  
        if result is not None:
            print(result)  

if __name__ == '__main__':
    main()
