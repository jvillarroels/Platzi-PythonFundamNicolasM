import random

print("")
print("Programa 0_main.py")
# print("Clase 17 Operador lógico not")
print("=====================")
print("")

options = ('piedra', 'papel', 'tijera')

user_option = input('Piedra, papel o tijera => ')
user_option = user_option.lower()

computer_option = random.choice(options)

print('User option => ', user_option)
print('computer_option => ', computer_option)

if not user_option in options:
    print('*** ---> Esa opción no es válida')

if user_option == computer_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('piedra gana a tijera')
        print('user ganó')
    else:
        print('Papel gana a piedra')
        print('computer ganó ')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('papel gana a piedra')
        print('user ganó')
    else:
        print('tijera gana a papel')
        print('computer gano')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print('tijera gana a papel')
        print('user gano')
    else:
        print('piedra gana a tijera')
        print('computer ganó')

