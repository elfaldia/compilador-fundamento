# main.py
import lexer
import parser

def main():
    # Pedir datos de entrada
    print("Ingrese una expresión (por ejemplo: 3 + 4):")
    datosEntrada = input(">> ")

    # Inicializa el lexer
    entidadLexer = lexer.lexer
    entidadLexer.input(datosEntrada)

    # Muestra los tokens generados por el lexer
    print("\nTokens generados:")
    for token in entidadLexer:
        print(token)

    # Transformar la entrada usando el parser
    print("\nResultado del parser:")
    resultado = parser.parser.parse(datosEntrada)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
