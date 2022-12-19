def add(n,i,z,sum):
    n = int(input())
    i = 0
    z = []
    sum = 0
    for i in range(n):
        z.append(i+1)
    print(z)
    i = 1
    for i in range(n):
        z[i] = z[i]**3
        sum = sum + z[i]
    print(sum)
n = 0
i = 0
z = []
sum = 0
add(n,i,z,sum)