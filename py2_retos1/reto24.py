palabra=input("Escribe la palabra a evaluar: ").lower()
if palabra==palabra[::-1]:
  print("La palbra", palabra, "es un Palíndromo")
else:
  print("La palabra",palabra,"no es un Palíndromo")