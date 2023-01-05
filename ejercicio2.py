A = [20, 15, 12, 11, 8, 4, 1]

maxi = 20
mini = maxi
for i in A:

    if i<mini:
        mini=i
    print ("El promedio más bajo es:",mini)
    A.remove(mini)
    print (A)
suma = 0
for j in A:
    suma+=j
print (suma)
print (suma/len(A))