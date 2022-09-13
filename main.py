import time

num1 = 10
num2 = 30
num3 = 5.5

print("Varibales numéricas: integer y float")
print ("numero 1:",num1, "numero 2:",num2, "numero 3:",num3)
time.sleep(2)
# Al ser ambas variables numéricas, podemos realizar operaciones matemáticas con ellas:
print("\nResultados Integer")
print("numero1 * numero2:", num1 * num2)
print("numero1 + numero2:", num1 + num2)
time.sleep(2)
# La división entre 2 int aplica al resultado una "tranformación instantánea a "float", ya que el número puede contener decimales:

print("\nResultado en float:")
print(num2 / num1)

# Textos: string (str)
texto1 = "Python es un"
texto2 = "lenguaje de programacion"

print("\nVariables de texto string")
print(texto1 , texto2)
# Los textos son un tipo de datos particular, ya que cuando una variable es de tipo String, se abre a un mundo de funciones o métodos asociados que permiten realizar muchas operaciones con ellas, desde cortarlas, buscar caracteres en su interior y muchas otras, que si quieres explorar, están listadas y explicadas aquí: https://www.w3schools.com/python/python_strings.asp

print("\nupper():", texto1.upper())
print("\nreplace():", texto2.replace('g', 'G'))

#INGRESAR NUMERO
numero_usuario = input("ingrese su numero: " )

if numero_usuario.isnumeric():
  print("si es un numero")
else:
  print("no es un numero")










#ENTEROS (int)
entero = 7
print(type(entero))


#DECIMAL(double)
decimal = 5.5
print(decimal)
print(type(decimal))

#True (bool)
x=True
print(x)
print(type(x))

#TEXTO (string)
texto = "HOLA"
print (texto)
print (type(texto))