#  Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#  Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('5ex_file.txt', 'w+') as f:
    f.write(' '.join(('4234', '324', '12312\n')))
    f.seek(0)
    m_list = []
    for el in f.read().split():
        m_list.append(int(el))
    print(f'Sum: {sum(m_list)}')
    f.write(' '.join(('Sum:', str(sum(m_list)))))








