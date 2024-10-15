import time
import timeit

# Medir o tempo de execução com time - inicio
start_time = time.time()
n = 40

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# print(fib(n))
# Medir o tempo de execução com time - fim
end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução: {execution_time:.2f} segundos")


# Medir o tempo de execução com timeit
execution_time = timeit.timeit(lambda: fib(n), number=1)
print(f"Tempo de execução: {execution_time:.2f} segundos")



# fibonacci dynamic
n = 40
fib_cache = [-1 for i in range(n)]
fib_cache[0] = fib_cache[1] = 1
def fib_dynamic(n):
    if fib_cache[n -1] != -1:
        return fib_cache[n -1]
    fib_cache[n -1] = fib_dynamic(n - 1) + fib_dynamic(n - 2)
    return fib_cache[n -1]

print(fib_dynamic(n))


# Medir o tempo de execução com timeit
execution_time = timeit.timeit(lambda: fib_dynamic(n), number=1)
print(f"Tempo de execução: {execution_time:.10f} segundos")