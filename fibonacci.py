#! /usr/bin/python
# escribe la serie de Fibonacci hasta el numero

def fibonacci():
    print ("programa que calcula el Fibonacci dado un numero")
    numero = int(input("Ingrese el numero a calcular: "))
    a, b = 0, 1
    i=0
    print(a)
    while i < numero:
          print(b)
          a, b = b, a+b
          i = i+1
fibonacci()