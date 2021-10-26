# Esto es un programa en lenguaje Python.
# Las tres primeras líneas son comentarios, solo sirven para informar
# al lector, pero el intérprete de Python se las salta sin hacerles caso

print("Hola") # esta orden imprime un mensaje en pantalla

mi_dato = 5
print(mi_dato) # aquí guardamos un dato en una variable y se muestra.

dato = "Las variables pueden contener distintos tipos de datos"
print(dato)

mi_dato = dato
print(dato) # el contenido de una variable puede cambiarse

a = 4
b = 6
print(a+b) # Se puede operar con las variables,

a = '5'
b = '8'
print(a+b) # Pero ¡cuidado! Debemos tener cuidado con el tipo de dato.

a = 4.3        # esto es un número decimal
b = 'palabra'  # esto es una "cadena" de caracteres. no se puede sumar con
               # el anterior
c= (4, 3.2, "azul")

print(c)
