number = 23
guess = int(input('Введите целове число : '))

if guess == number:
    print('Поздравляю, вы угадали! ') # Начало нового блока
    print('(Хотя и не выиграли никакого приза!)') # Конец нового блока
elif guess < number:
    print('Нет, загаданное число немного больше этого. ') # Еще один блок
    # Внутри блока вы можете выполнять все, что угодно
else:
    print('Нет загаданное число немного меньше этого.')