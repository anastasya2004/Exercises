'''
Задание 9.
Дано предложение. В нем только два слова одинаковые. Найти эти слова.
'''
text = input()

text = text.split()

for i in text:
    cnt = text.count(i)
    if cnt == 2:
        print(i)
        break