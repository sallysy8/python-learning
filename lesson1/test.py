
def fib(n):
    a,b = 0,1
    for _ in range(n-1):
        next_num = a + b
        a , b = b, next_num
    return b




fib(5)