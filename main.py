BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

import time
iniciar_trivia = True
intentos = 0

print(MAGENTA+"BIENVENIDO A MI TRIVIA"+RESET)
print(MAGENTA+"Pondre en practica lo aprendido"+RESET)
puntaje = 0
#import random
#puntaje = random.randint(0, 5)
print("Iniciamos con puntaje: ",puntaje)

nombre = input("Ingresa tu nombre: ")

while iniciar_trivia == True:
  intentos += 1
  puntaje = 0
  print("\nIntento numero:", intentos)
  input("Precione Enter para continuar")
  print("Primera pregunta...")
  print("Imagina que aqui procede toda tu trivia")
  time.sleep(5)
  print("Jugando...")
  time.sleep(5)
  
  print (CYAN+" \n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa correcta y presiona 'Enter' para enviar tu respuesta: \n"+RESET)

#PRIMERA PREGUNTA
  print(BLUE+"1.- Quien fue el primer Inca?\n"+RESET)
  print( "a) Manco Capac")
  print( "b) Sinchi Roca")
  print( "c) Yoque Yupanqui")
  print( "d) Capac Yupanqui")

  time.sleep(2)
  respuesta_1 = input ("\nTu respuesta es: ")

  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_1 == "a":
    puntaje += 5
    print(GREEN+"Muy bien", nombre, "!"+RESET)
  else:
    puntaje -= 5
    print(RED+"Incorrecto", nombre, "!"+RESET)
  
#print("\nGracias", nombre, "por jugar mi trivia. Tu puntaje es: ", puntaje)

  print(nombre, "llevas", puntaje, "puntos")

#SEGUNDA PREGUNTA CON RESPUESTA SECRETA
  print(BLUE+"\n2.- Quien fue el primer Virrey del Peru? \n"+RESET)
  print("a) Antonio de Mendoza")
  print("b) Francisco de Toledo")
  print("c) Jose de la Serna de Hinojosa")
  print("d) Blanco Nuñez de Vela")

  time.sleep(2)
  respuesta_2 = input("\n Tu respuesta es: ")
  while respuesta_2 not in ("a", "b", "c", "d", "e"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta:")

  if respuesta_2 == "a":
    puntaje -= 5
    print (RED+"Incorrecto", nombre, "!\nAntonio de Mendoza fue el 2do Virrey"+RESET)
  elif respuesta_2 == "b":
    puntaje -= 5
    print(RED+"Incorrecto", nombre, "!\nFrancisco de Toledo fue el 5to Virrey"+RESET)
  elif respuesta_2 == "c":
    puntaje -= 5
    print(RED+"Incorrecto", nombre, "!\nJose de la Serna de Hinojosa fue el ultimo virrey"+RESET)
  elif respuesta_2 == "d":
    puntaje += 5
    print(GREEN+"Muy bien", nombre, "!"+RESET)

  else:
    puntaje += 10
    print("Respuesta secreta: El Peru tuvo 40 Virreyes")
  
  print(nombre, "llevas", puntaje, "puntos")

#TERCERA PREGUNTA
  print(BLUE+"\n3.- Quien fue el primer presidente del Peru? \n"+RESET)
  print("a) Alan Garcia Perez ")
  print("b) Jose de la Riva Aguero")
  print("c) Nicolas de Pierola")
  print("d) Fernando Belaunde Terry")

  time.sleep(2)
  respuesta_3 = input("\n Tu respuesta es: ")
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta:")

  if respuesta_3 == "a":
    puntaje = puntaje / 2
    print (RED+"Disparatada", nombre, "!se te divide entre 2\nPresidente de (1985 - 1990) y en (2006 - 2011)"+RESET)
  elif respuesta_3 == "b":
    puntaje = puntaje * 2
    print(GREEN+"Correcto", nombre, "!se te mutiplica el puntaje"+RESET)
  elif respuesta_3 == "c":
    puntaje = puntaje + 5
    print(RED+"Incorrecto", nombre, "!se te suma 5 puntos \n Presidente en 1895 - 1899"+RESET)
  else:
    puntaje = puntaje - 5
    print(RED+"Totalmente incorrecto", nombre, "! se te resta 5 puntos \nPresidente en (1980 - 1985)"+RESET)

  print(nombre, "llevas", puntaje, "puntos")

#JUEGO DE NUMEROS

  print(BLUE+"\n4.- Juego Aritmetico\n"+RESET)

  def ejercicio1():
    x = int(input("Ingrese el primer numero: "))
    y = int(input("ingrese el segundo numero: "))
    print("El promedio de",x, "y", y, "es: ", ((x + y)/2))

  def ejercicio2():
    x = int(input("Ingrese el primer numero: "))
    y = int(input("ingrese el segundo numero: "))
    print( x,"elevado a ", y, "es: ", (x**y))

  def ejercicio3():
    x = int(input("Ingrese el primer numero: "))
    print("Raiz cuadrada de",x,":",(x**(1/2)))

  print("Ingrese numero (1,2 o 3) de ejercicio: ")
  num = int(input())
  
  if num == 1:
    ejercicio1()
  elif num == 2:
    ejercicio2()
  elif num == 3:
    ejercicio3()

  time.sleep(3)

  print(GREEN+"\nGracias", nombre, "por jugar mi trivia")
#puntaje
  if puntaje >= 0:
    print (nombre,"llevas",puntaje, "punto positivo")
  else:
    print(nombre,"llevas",puntaje, "punto negativos")
#repetir trivia
  print("Excelente, has obtenido",puntaje, "puntos"+RESET)
  print("\nDesea intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":
    print(MAGENTA+"\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!"+RESET)
    iniciar_trivia = False