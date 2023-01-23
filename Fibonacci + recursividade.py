from os import system
system ('cls')
# Livraria e comando para limpar o terminal.
# Deixa o terminal mais limpo e fácil de visualizar.
    
def fibonacci (num):
    if num <= 1:
        return num
    else:
        return fibonacci (num-1) + fibonacci(num-2)

num = int(input())

for x in range (num):
    if x == 0 or x == 1:
        print (fibonacci (x), end=' ')
        
    elif x == num - 1:
        print (fibonacci (x))
        
    else:
        print (fibonacci (x), end=' ')