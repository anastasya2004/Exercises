'''
Задание 10.
Дано предложение. Выведите на экран те слова, которые отличны от первого слова,
в слове нет повторяющихся букв 
#и это слово симметрично.
'''
text = input()

text = text.split()

for i in text:
    if text[0] != i and len(set(i)) == len(i):
        print(i)
        
#and i == i[::-1]