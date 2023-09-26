'''
Задание 7.
Дано предложение. Найти длину его самого короткого слова.
'''
text = input()

list = text.split()
long = []

for word in list:
    lw = len(word)
    long.append(lw)
    
print(min(long))