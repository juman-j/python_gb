# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
str_1 = ['This ', 'is ', 'first ', 'str\n', 'This ', 'is ', 'second ', 'str\n', 'This ', 'is ', 'third ', 'str']

with open('2ex_file.txt', 'w') as file:
    file.writelines(str_1)

with open('2ex_file.txt', 'r') as file:
    count_str = sum(1 for _ in file)
    print(f'Количество строк в файле "{file.name}": {count_str}')
    file.seek(0)
    n = 0
    while n < count_str:
        el = file.readline().split(' ')
        print(f'Количество слов в {n + 1} строке: {len(el)}')
        n += 1







