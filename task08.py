'''3
Задание 8.
Дано предложение. Напечатать все его слова в порядке неубывания их длин.
'''
text = input()

text = text.split()

print(sorted(text, key=len))