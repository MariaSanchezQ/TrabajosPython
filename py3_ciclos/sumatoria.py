def sumatoria (A,B,C):
  n = len(A)
  suma = 0
  for i in range(n):
    d = A[i]*B[i]
    e = d + C[i]
    suma = suma + e
  total = suma + n**2
  print('La suma es',str(total))

A = [2,4,3]
B = [1,5,7]
C = [7,5,1]
sumatoria(A,B,C)
