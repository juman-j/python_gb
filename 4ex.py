# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('4ex_file_new.txt', 'w', encoding='utf-8') as nf:
    with open('4ex_file.txt', 'r', encoding='utf-8') as mf:
        count_str = sum(1 for _ in mf)
        mf.seek(0)
        n = 0
        while n < count_str:
            line = mf.readline()
            nf.write(str([line.replace(line.split()[0], my_dict.get(line.split()[0]))]))
            print(line)
            n += 1






