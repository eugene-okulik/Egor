number = 78

while True:
    user_input = int(input('Введите число: '))
    if user_input != number:
        print('Попробуйте снова!')
        continue
    else:
        print('Поздравляю! Вы угадали!')
        break
