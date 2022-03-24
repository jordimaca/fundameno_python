def reverso(x):
  return x[::-1]

nombre = input("Digame su nombre completo y se lo mostrare alrevez = ")
nombre = reverso(nombre)
print (nombre)