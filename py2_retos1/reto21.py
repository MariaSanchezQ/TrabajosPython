def BMI(a,b):
  a=a/100
  imc = b/(a**2)
  if(imc <18.5):
    print("Su masa corporal es de ", str(imc), "y su peso es inferior al normal")
  elif (imc>= 18.5 and imc <= 24.9):
    print("Su masa corporal es de ", str(imc), "y su peso es normal")
  elif (imc >=25 and imc <= 29.9):
    print("Su masa corporal es de ", str(imc), "y su peso es superior al normal")
  elif(imc>=30):
    print("Su masa corporal es de ", str(imc), "y se encuentra en estado de obesidad")
  

estatura = float(input("Ingrese su estatura en cm: "))
peso = float(input("Ingrese su peso en Kg: "))

BMI(estatura,peso)