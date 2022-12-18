def year(years):
    if ((years % 4 == 0) and years % 100 != 0) or years % 400 == 0:
        print("Високосный")
    else:
        print("Невисокосный")

years = int(input())
year (years)