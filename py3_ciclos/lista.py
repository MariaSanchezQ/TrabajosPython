def lista (A,B):
  n = len(A)//2
  C =[]
  for i in range(n):
    e = (A[i+1]**2)*B[2*i]
    g = e + B[n+i]
    C.append(g)
  print('C =', C)


A=[2,3,5,-8]
B=[1,2,8,7]
lista(A,B)