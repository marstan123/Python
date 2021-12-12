def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно')
    else:
        print(b, 'максимально')
printMax(3, 4) #пряма передача значений

x = 5
y = 7
z = 10
w = 10

printMax(x, y) #передача переменных в качестве аргументов
printMax(y, z)
printMax(z, w)