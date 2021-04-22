def bisiesto(a):
  b = a%4
  if(b == 0):
    print("El año es bisiesto")
  else:
    print("El año no es bisiesto")


a= int(input("Escriba el año a evaluar: "))
bisiesto(a)