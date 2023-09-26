'''
Задание 12.
Как известно, имя в языке Python может содержать только латинские символы, цифры
и знак подчеркивания "_". При этом, имя не может начинаться с цифры и не может быть
ключевым словом. Напишите программу, которая проверяет введенную строку, может ли
она быть именем в языке Python.
'''
str = input()
text = list(str)

key = ['False', 'class', 'from', 'or', 'None', 'continue', 'global', 'pass', 'True', 'def', 'if', 'raise', 'and', 'del', 'import', 'return', 'as', 'elif', 'in', 'try', 'assert', 'else', 'is', 'while', 'async', 'except', 'lambda', 'with', 'await', 'finally', 'nonlocal', 'yield', 'break', 'for', 'not']

k = 2
if key.count(str):
    k = 1
else:
    k = 0

    
for i in text:
    if text[0] == "0" or text[0] == "1" or text[0] == "2" or text[0] == "3" or text[0] == "4" or text[0] == "5" or text[0] == "6" or text[0] == "7" or text[0] == "8" or text[0] == "9" or k == 1:
        rez = "false"
        break
    
    if ord(i) < 200 or i == "_" or i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
        rez = "true"
    else:
        rez = "false"
        
if rez == "true":
    print('Данная строка может быть именем')
else:
    print('Данная строка не может быть именем')