import random
a = random.randrange(1,120)
if a >= 10 and a <= 50:
  print('El número se encuentra en el intervalo entre 10 y 50: ', a)
if a > 50 and a <= 100:
  print ('El número se encuentra en el intervalo entre 51 y 100: ', a)
if a < 10:
  print ('El número es menor a 10: ', a)
if a > 100:
  print ('El número es mayor a 100: ', a)