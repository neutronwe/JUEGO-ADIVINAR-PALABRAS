import random

Sistemas = ["programacion", "ingenieria", "computador", "tecnologia", "computacion"]
Animales = ["perro", "gato", "conejo"]
Deportes = ["baloncesto", "futbol", "voleibol"]
Categorias = [Sistemas, Animales, Deportes]
Elegir = random.choice(Categorias)
Subelegir = random.choice(Elegir)
if Elegir == Sistemas:
  print("La Categoria de la palabra es: Sistemas")
elif Elegir == Animales:
  print("La Categoria de la palabra es: Animales")
else:
  print("La Categoria de la palabra es: Deportes")

letras_adivinar=[]
while True:
    letra = input("Ingrese una letra para descubrir la palabra: ")
    letras_adivinar.append(letra)
    palabra_oculta =""
    for c in Subelegir:
      if c in letras_adivinar:
        palabra_oculta+=c
      else:
        palabra_oculta+="_"
    print(palabra_oculta)