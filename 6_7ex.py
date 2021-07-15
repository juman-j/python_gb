#  Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
#  но с прописной первой буквой.
#  Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func()


# def int_func():
#     """
#     Функция приводит первую букву каждого слова в верхний регистр, а все остальные в нижний.
#     """
#     text = input('пару слов туда сюда: ').title()
#     return text
#
#
# print(int_func())


def int_func(word):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if set(word).difference(latin_char) else False


words = input('rr: ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), " ")
