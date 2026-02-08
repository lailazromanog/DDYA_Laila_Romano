
def main():
   n = input("Ingrese los datos de los estudiantes: ")
   datos = n.split()
   #separar los datos que ingresaron
   nombres = []
   notas = []

   for i in range(len(datos),2):
      nombre = datos[i] #nombre en posiciones pares, 0 es par
      nombres.append(nombre)
      nota = float(datos[i + 1]) #las notas en posiciones impares i+1
      notas.append(nota)


   if len(notas)>0:
      prom_general = sum(notas)/len(notas)
      print("Los estudiantes que estan por encima del promedio y aprobaron son:")
      for i in range(len(notas)):
         if notas[i] >= prom_general:
            print(nombres[i])
   else:
      print("No se ingresaron datos.")
   print("Finalizamos, vuelva pronto.")

main ( )