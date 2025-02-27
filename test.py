print ("Hola este es un archivo de pruebas")
a=20
b=30
if a > b:
    print(f"El valor es mayor a {a}")
else:
    print(f"El valor es menor a {b}")

def restar(a,b):
    print(f"vamos a restar {a} {b}")
    return a-b
restar(a,b)