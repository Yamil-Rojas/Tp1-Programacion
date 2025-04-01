
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla.

nombre = input("Ingresa tu nómbre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingresá tu nómbre: ")
apellido = input("Cual es tu apellido: ")
edad = input("¿cuantos años tenes?: ")
lugar = input("¿De donde sos?: ")
print(f"Hola soy {nombre} {apellido}, tengo {edad} años y soy de {lugar}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Ingrese el radio: "))
pi = 3.1416
area = pi * (radio**2)
perimetro = pi * (radio * 2)

print(f"El area de un circulo es: {area} y su perímetro es: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = float(input("ingrese la cantidad de segundos que desee: "))
horas = float(segundos / 3600)
print(f"El número que usted ingresó, equivale a {horas:.2f} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número. 

numero = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#    pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.     

num1 = int(input("Ingrese el primer número (No puede usar 0): "))
num2 = int(input("Ingrese el segundo número (No puede usar 0): "))

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
division = num1 / num2

print(f"La suma de ambos es: {suma}")
print(f"La división de ambos es: {division:.2f}")
print(f"La multiplicación de ambos es: {producto}")
print(f"La resta de ambos es: {resta}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: (ver dibujo)  

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura **2)
print(f"Su índice de masa corporal es: {imc:.2f}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#    pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: (ver dibujo)

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura ingresada en Celsius equivale a {fahrenheit:.2f} grados Fahrenheit")

# 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los 3 números es: {promedio:.2f}")