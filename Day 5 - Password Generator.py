import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!")
total_letters = int(input("How many letters would you like in your password? "))
total_symbols = int(input("How many symbols would you like? "))
total_numbers = int(input("How many numbers? "))

#Mezclar listas originales
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

#Teniendo en cuenta número seleccionado para cada tipo de elemento, se crea una lista en la que se guardará la selección.
seleccion = [] #Lista donde guardo todos los caracteres para la contraseña

#Creo un loop para guardar cada elemento en la lista
for sym in range(0,total_symbols):
    seleccion.append(symbols[sym])

for letra in range(0,total_letters):
    seleccion.append(letters[letra])

for num in range(0,total_numbers):
    seleccion.append(numbers[num])

#Combino la lista de seleccion
random.shuffle(seleccion)

#Uno los elementos de la lista y la paso a cadena de caracteres para hacer la contraseña
password = ''.join(seleccion)
print(f"Here is your password: {password}")