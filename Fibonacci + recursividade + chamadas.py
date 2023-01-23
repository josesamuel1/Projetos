from os import system
system ('cls')
# Livraria e comando para limpar o terminal.
# Deixa o terminal mais limpo e fácil de visualizar.

def fibonacci (x):
    global calls
    calls += 1
    
    if x <= 1:
        return x
    else:
        return fibonacci (x-1) + fibonacci(x-2)

rep = int (input ("Repetições: "))

for _ in range (rep):
    calls = 0
    fib = int (input ())
    result = fibonacci (fib)
    
    print (f'fib({fib}) = {result} = {calls-1} calls')