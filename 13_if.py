print("")
print("Programa 13_if.py")
print("Clase 18 Condicionales")
print("=====================")
print("")

if True: 
    print('debería ejecutarse')

if False:
    print('nunca se ejecuta')


pet = input('Cuál es tu mascota favorita? ')

if pet == 'perro':
    print('genial tienes buen gusto')

elif pet == 'gato':
    print('espero tegngas suerte')

elif pet == 'pez':
    print('eres lo máximo')
else:
    print('no tienes ninguna mascota interesante')

'''
stock = int(input('Digita el stock => '))

if stock >= 100 and stock <=1000:
    print('el stock es correcto')
else:
    print('el stock es incorrecto')
'''

number = int(input('Ingrese un numero => '))
result = number % 2
if (result == 0):
    print('Es par')
else: 
    print('Es impar')
