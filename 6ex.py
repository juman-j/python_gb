# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

from itertools import cycle, count

nl = []
for i in count(0):
    if i == 11:
        break
    nl.append(i)
print(nl)


my_list = []
el = 0
for i in cycle(['Hello', 'my', 'dear', 'friend', 'I', 'missed', 'you', 'so', 'much']):
    if el == 18:
        break
    my_list.append(i)
    el += 1
print(my_list)


