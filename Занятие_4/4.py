def add(N,i,z,summ):
    for i in range(N):
        z.append(int(input()))
    print(z)
    i = 1
    for (i) in range(N):
        summ = summ + z[i]
    print(summ)
N = int(input())
i = 0
z = []
summ = 0
add(N,i,z,summ)