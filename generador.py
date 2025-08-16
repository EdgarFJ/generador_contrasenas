import random # Importa el módulo para generar valores aleatorios
import string # Importa el módulo con conjuntos de caracteres predefinidos

# Función que genera una contraseña segura
def generar_contraseña(longitud=12, mayus=True, minus=True, numeros=True, simbolos=True):
    caracteres = ""  # Inicializa la cadena que contendrá todos los caracteres posibles
    if mayus:
        caracteres += string.ascii_uppercase
    if minus:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Selecciona al menos un tipo de caracter."

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == "__main__":
    print("=== Generador de Contraseñas Seguras ===")
    longitud = int(input("Longitud de la contraseña: "))
    contraseña = generar_contraseña(longitud)
    print(f"Tu nueva contraseña es: {contraseña}")
