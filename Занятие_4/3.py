def add(a,b):
    while a != b:
       a -= 1
       if a % 2 != 0:
           print(a)
a = int(input())
b = int(input())
add(a,b)