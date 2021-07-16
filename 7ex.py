# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

# Пример списка:
# [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
import statistics
import json

my_dict = {}
positive_profit = []
with open('7_file_json.json', 'w') as ff:
    with open('7ex_file.txt', 'r+') as f:
        for line in f:
            name, profit = line.split()[0], (int(line.split()[2]) - int(line.split()[3]))
            my_dict[name] = profit
        for n in my_dict.values():
            if n >= 0:
                positive_profit.append(n)
        aver_profit_dict = {'average profit': statistics.mean(positive_profit)}
        my_list = [my_dict, aver_profit_dict]
        print(my_list)
        json.dump(my_list, ff, ensure_ascii=False, indent=4)




