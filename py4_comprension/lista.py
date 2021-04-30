A=[2,3,5,-8]
B=[1,2,8,7]
C=[]
n = len(A)//2
C=[(A[i+1]**2)*(B[2*i])+B[n+i] for i in range(n)]
print('C =',C)
