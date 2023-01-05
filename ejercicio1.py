


A = int(input(u"Ingrese el tamaño de los arreglos"))
B = []
C = []
for i in range (0,A):
 B.append(input("Ingrese nombre de las personas"))
print (B)
for j in range (0,A):
 C.append(len(B[j]))
print (C)