'''
Задание 2.
Дан текст. Необходимо определить максимальное количество последовательных одинаковых символов в нём.
'''
text = input()

cnt = 0 
max = 0

for i in range(len(text)):
    if text[i] == text[i-1]:
        cnt += 1 
    else:
        cnt = 0 
    if cnt > max:
        max = cnt
print(max + 1)