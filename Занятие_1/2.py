age = int(input('Ваши возраст: '))
name = input('Ваше имя:')

if 0 < age < 75 and name != 'Иван':
    if age >= 16:
        print('Поздравляем, Вы во ВГУИТ')
    else:
        print('Сначала надо окончить школу. Еще лет учиться: ' + str(16 - age))