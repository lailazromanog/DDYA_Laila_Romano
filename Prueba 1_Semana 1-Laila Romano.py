
def main():
    n = int(input("Ingrese un número: "))
    #Primera parte
    if n > 0:
        print("El número es positivo.")
    elif n < 0:
        print("El número es negativo.")
    else: 
        print("El número es cero.")
    #Numero primo
    if n > 1:
        divisor = 2
        es_primo = True
        while divisor * divisor <= n:
            if n % divisor == 0:
                es_primo = False
                break #termina ahi
            divisor = divisor + 1
        if es_primo:
            print("El número  es primo.")
    #Fibinacci
    casos_base =  [0,1]
    while casos_base[-1] < n:
        n_proximo = casos_base[-1] + casos_base[-2]
        casos_base.append(n_proximo)
    if n in casos_base:
        print("Es un número Fibonacci")
    print("Finalizamos, vuelva pronto.")
main ( )