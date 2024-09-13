# Ejemplo de conversion de tipos de datos
entero = 10
decimal = 10.5
cadena = "25"

# Convertir cadena a entero
cadena_a_entero = int(cadena)
print(f"Cadena a entero: {cadena_a_entero}")

# Convertir entero a cadena
entero_a_cadena = str(entero)
print(f"Entero a cadena: {entero_a_cadena}")

# Convertir decimal a entero (truncando la parte decimal)
decimal_a_entero = int(decimal)
print(f"Decimal a entero: {decimal_a_entero}")

# Multilineas de cadenas
cadena_multilinea = """Este es un ejemplo
de una cadena multilinea.
Puede ocupar varias lineas 
y conservar el formato.
"""
print("Cadena multilinea:")
print(cadena_multilinea)

# Funcion len()
cadena_simple = "Hola, mundo!"
longitud = len(cadena_simple)
print(f"La longitud de la cadena '{cadena_simple}' es: {longitud}")

# Sub cadenas
primeros_n_caracteres = cadena_simple[:5]  # Obtener los primeros 5 caracteres
print(f"Primeros 5 caracteres: {primeros_n_caracteres}")

en_medio_caracteres = cadena_simple[6:11]  # Obtener caracteres del medio
print(f"Caracteres del medio: {en_medio_caracteres}")

ultimos_n_caracteres = cadena_simple[-6:]  # Obtener los ultimos 6 caracteres
print(f"Ultimos 6 caracteres: {ultimos_n_caracteres}")

# Funcion upper()
cadena_upper = cadena_simple.upper()
print(f"Cadena en mayusculas: {cadena_upper}")
# Funcion lower()
cadena_lower = cadena_simple.lower()
print(f"Cadena en minusculas: {cadena_lower}")

# Funcion strip()
cadena_con_espacios = "   Hola como van    "
cadena_strip = cadena_con_espacios.strip()
print(f"Cadena sin espacios al inicio y al final: '{cadena_strip}'")

# Funcion replace()
cadena_reemplazada = cadena_simple.replace("mundo", "Python")
print(f"Cadena reemplazada: {cadena_reemplazada}")

# Funcion split()
cadena_split = cadena_simple.split(",")
print(f"Cadena dividida por ',': {cadena_split}")

# Formato de cadenas F-String
nombre = "Oscar"
edad = 20
cadena_f_string = f"Mi nombre es {nombre} y tengo {edad} años."
print(cadena_f_string)

