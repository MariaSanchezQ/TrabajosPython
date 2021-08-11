C=[];
a=int(input("Ingrese un valor entero: "));
C.append(a);

while (a != 1):
  if a%2 ==0:
    a = a/2;
  else:
    a = a*3 + 1;
  C.append(a);


print(C);