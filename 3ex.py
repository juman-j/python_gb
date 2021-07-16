# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


with open('3ex_file.txt') as f:
    count_str = sum(1 for _ in f)
    f.seek(0)
    my_dict = {}
    n = 0
    while n < count_str:
        mini_list = f.readline().split(' ')
        list_to_dict = {mini_list[0]: float(mini_list[1])}
        my_dict.update(list_to_dict)
        n += 1

print(f'Работники с зарплатой ниже 20к: {[el[0]for el in my_dict.items() if el[1] < 20000]}')
print(f'Средняя зарплата: {sum(my_dict.values())/count_str}')
