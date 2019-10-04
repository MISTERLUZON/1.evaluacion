#En este programa le pedimos al usuario
#que teclee los coeficientes de un polinomio
#y hallamos el valor de las raices
import math
def ecuacion():
    print "Introduzca los coeficientes de el polinomio"
    print "A^2+B*x+C=0"
    a=input("A= ")
    b=input("B= ")
    c=input("C= ")
    radicando=b*b-4*a*c
    if (radicando>0):
        raiz1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        raiz2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
        print "primera solucion= " , raiz1
        print "segunda solucion= " , raiz2
    else:
        print "Esta ecuacion no tiene una solucion real"

ecuacion()
 
 

