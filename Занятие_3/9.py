def shok(n, m, k):
    if (k % n == 0 or k % m == 0) and (k < n * m):
        print('Да')
    else:
        print("Нет")
n = int(input())
m = int(input())
k = int(input())
shok(n, m, k)