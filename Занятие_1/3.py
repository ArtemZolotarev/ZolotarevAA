second = int(input('Введите количество секунд: '))
min = second//60
hour = min//60
day = hour//24

print(str(second) + 'Секунд это ' + str(day))