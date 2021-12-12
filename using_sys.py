import sys

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)
print('\n\nПеременная PYTONPATH содержит', sys.path, '\n')