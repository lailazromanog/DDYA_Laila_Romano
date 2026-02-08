
#esto es una prueba N2
def main():
   n = input("Ingrese los datos de los estudiantes: ")
   datos = n.split()
   #separar los datos que ingresaron
   nombres = []
   notas = []
   for i in range(0,len(datos),2):
      nombre = datos[i] #nombre en posciones pares, 0 es par
      nombres.append(nombre)
      nota = float(datos[i + 1]) #las notas en posiciones impares i+1
      notas.append(nota)

   print("Los estudiantes que aprobaron son:")
   for i in range(len(notas)):
      if notas[i] >=3.0:
         print(nombres[i])
   print("Finalizamos, vuelva pronto.")
main ( )
