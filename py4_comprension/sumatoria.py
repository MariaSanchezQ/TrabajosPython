A = [2,4,3]
B = [1,5,7]
C = [7,5,1]

n= len(A)
a = sum((A[i]*B[i]+C[i] for i in range(n)))+n**2
print(a)