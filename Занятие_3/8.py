def sovpad(a, b, c):
    if a == b and a == c and b == c:
        print('3')
    elif a == b or a == c or b == c:
        print('2')
    else:
        print('0')
a = int(input())
b = int(input())
c = int(input())
sovpad(a, b, c)