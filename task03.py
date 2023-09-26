'''
Задание 3.
Дан текст. Определить, сколько различных букв в нем.
'''
##text = input()
##print(len(set(text)))


text = input() 

list = [] 

for letter in text: 
    if letter not in list: 
        list.append(letter) 

print(len(list)) 