
def fib(n):
    if(n<=1):
        return n
    
    return fib(n-2) + fib(n-1)

fib(6)

imprimir = [fib(i) for i in range(10)]

print(imprimir)