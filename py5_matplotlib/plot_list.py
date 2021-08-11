print("Ejercicio 5 Python: Plot List - Matplotlib");
print(" ");
C=[];
a=int(input("Ingrese un valor entero: "));
C.append(a);
print(" ");

while (a != 1):
  if a%2 ==0:
    a = a/2;
  else:
    a = a*3 + 1;
  C.append(a);

print(C);
print(" ");
print("El programa ha finalizado.");