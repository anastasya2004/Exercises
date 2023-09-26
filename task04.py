'''
Задание 4.
Определите какой символ встречается ровно три раза в тексте. Гарантируется, что символ
с такой частотой встречаемости только один.
'''
text = input()

list = []
cnt = []

for letter in text: 
    if letter not in list: 
        list.append(letter) 

for c in list:
    k = text.count(c)
    cnt.append(k)

ind = cnt.index(3)

print(list[ind])