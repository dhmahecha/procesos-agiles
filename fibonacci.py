#! /usr/bin/python
# escribe la serie de Fibonacci hasta el numero

def fibonacci():
    print ("programa que calcula el Fibonacci dado un numero")
    numero = int(input("Ingrese el numero a calcular: "))
    a, b = 1, 2
    print(a)
    while b < numero:
          print(b)
          a, b = b, a+b
fibonacci()