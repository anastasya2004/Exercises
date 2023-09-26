'''
Задание 6.
Дано предложение. Напечатать его в обратном порядке слов.
'''
ptr = input()
words = ptr.split()
rez = " ".join(words[::-1])
print(rez)