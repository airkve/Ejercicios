# Ejemplo para resolver Fibonacci
# fibonacci(N)= fibonacci(N-1)+fibonaci(N-2)

def fibonacci(num):
    if num != 1 and num != 0:
        return fibonacci(num - 1) + fibonacci(num - 2)
    else:
        return 1

for i in range(20):
    print(fibonacci(i))