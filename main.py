def hello(name):
    return "Hola " + name

# Pedir datos al usuario
name = str(input("Tu nombre: "))

# Mostrar resultado con f-string
print(hello(name))