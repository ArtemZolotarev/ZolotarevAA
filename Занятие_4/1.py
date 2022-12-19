def add(a,b):
    if a < b :
        print(a)
        while a != b:
            a += 1
            print(a)
a = int(input())
b = int(input())
add(a,b)