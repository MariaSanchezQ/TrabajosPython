def bisiesto(a):
  if(a%4 == 0 and (not(a%100==0) or a%400==0)):
    print("El año", str(a),"es bisiesto")
  else:
    print("El año",str(a)," no es bisiesto")


a= int(input("Escriba el año a evaluar: "))
bisiesto(a)