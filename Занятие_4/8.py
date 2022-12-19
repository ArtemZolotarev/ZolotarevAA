def add(n):
    n = int(input())
    if n <=9:
        for i in range(1, n + 1):
            for p in range(1, 1 + i):
                print(p, end="")
            print()
    else:
        print("Слишком большое число")
n = 0
add(n)