def add(n,factorial):
    n = int(input())
    factorial = 1
    while n > 1:
        factorial = factorial * n
        n -= 1
    print(factorial)
n = 0
factorial = 0
add(n,factorial)