Lista1 = []
Lista2 = []
ListaTotal = []
for a in range (0, 11):
  Lista1.append(a)

for b in range (11, 21):
  Lista2.append(b)
  
ListaTotal = Lista1 + Lista2;

print("Lista Numeros 0 - 10")
print (Lista1)
print(" ")
print("Lista Numeros 11 - 20")
print (Lista2)
print(" ")
print("Lista con todos los numeros")
print (ListaTotal)

