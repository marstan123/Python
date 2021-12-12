def total(initial=1, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count *= extra_number
    print(count)
total(10, 1, 2, 3, extra_number=2)
# Вызовет ошибку, посколько мы не указали значение
# аргумента по умолочанию для extra_number