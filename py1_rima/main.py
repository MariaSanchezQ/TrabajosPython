import re

print ('hola mundo')

archivo = open('palabras500.csv',encoding="utf-8")
lineas = archivo.readlines()
archivo.close()

print(len(lineas))

def rima():
  for i in lineas:
    if i[-2] == 'n':
      if i[-3] == 'a':
        print(i)

rima()
#print(lineas)