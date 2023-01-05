filas1=int(input("introduce numero de finlas de la matriz 1: "))
colum1=int(input("introduce numero de columnas matriz 1: "))
colum2=int(input("introduce numero de columnas matriz 2 : "))
A=[]
for i in range (filas1):
    A.append([0]*colum1)

for i in range(filas1):
    print(A[i])

B=[]
for i in range(colum1):
    B.append([0]*colum2)

for i in range(colum1):
    print(B[i])

for i in range(filas1):
    for j in range(colum1):
        A[i][j]=float(input("introduce el componente (%d,%d): "%(i,j)))

for i in range(filas1):
    print(A[i])

for i in range(colum1):
    for j in range(colum2):
        B[i][j]=float(input("introduce el componente (%d,%d): "%(i,j)))
for i in range(colum1):
    print(B[1])

C=[]
for i in range(filas1):
    C.append([0]*colum2)
for i in range(filas1):
    print(C[i])

for i in range(filas1):
    for j in range(colum2):
        for k in range(colum1):
            C[i][j]+=A[i][k]*B[k][j]

for i in range(filas1):
    R=[]
    for j in range(colum2):
        R.append(C[i][j])
    print(R)


