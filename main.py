import ply.lex as lex
import ply.yacc as yacc
from lexer import lexer  # Importa el lexer definido
from parser import parser  # Importa el parser definido

def main():
    # Ruta del archivo con código Trolleangue
    archivo = './ejemplo.txt'

    try:
        # Leer el contenido del archivo
        with open(archivo, 'r', encoding='utf-8') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'")
        return
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    # Mostrar el contenido del archivo (opcional, para depuración)
    print("Código a compilar:")
    print(data)
    print("\n--- Compilando ---\n")

    # Ejecutar el parser para compilar y ejecutar el código
    try:
        result = parser.parse(data)
        print("\n--- Ejecución Completada ---\n")
        print("Resultado del parser:")
        print(result)
    except Exception as e:
        print(f"Error durante la compilación: {e}")

if __name__ == '__main__':
    main()
