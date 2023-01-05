# importamos la bibliteca NumPy
import numpy as np
    
def main():
  # declaremos y construyamos una matriz
  # 2x3 (dos filas y tres columnas)
  matriz = np.array([(3, 5, 7), (1, 2, 9)])
     
  # vamos a mostrar los valores de la matriz
  print("Elementos de la matriz:")
  for i in range(np.shape(matriz)[0]):
    for j in range(np.shape(matriz)[1]):
      print("%7.2f" % matriz[i][j], end="")
     
    print()
 
  # transpongamos la matriz usando el método transpose()
  transpuesta = matriz.transpose() 
     
  # vamos a mostrar los valores de la matriz transpuesta
  print("\nElementos de la matriz transpuesta:")
  for i in range(np.shape(transpuesta)[0]):
    for j in range(np.shape(transpuesta)[1]):
      print("%7.2f" % transpuesta[i][j], end="")
     
    print()  
 
if __name__== "__main__":
  main()