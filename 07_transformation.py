print("")
print("Programa 07_transformation.py")
print("Leccion 11 Transformación de tipos")
print("=====================")
print("")

name = "Nicolas"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print("Nicolas" + " Molina")
print(10 + 20)
print("Nicolas" + "12")

age = 12
print("Mi edad es " + str(age))

print(f"Mi edad es {age}")

age = input("Escribe tu edad => ")
print(type(age))
print(type(age))
age = int(age)
age += 10
print(f"tu edad en 10 años será {age}")
