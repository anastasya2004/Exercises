'''
Задание 5.
Даны три строки. Выведите на экран только те символы, которые есть лишь в одной из этих трёх строк.
'''
one = input()
two = input()
three = input()

str = one + two + three
list = ""

for l in one: 
    if l not in two and l not in three: 
        list += l
        
for l in two: 
    if l not in one and l not in three: 
        list += l
        
for l in three: 
    if l not in one and l not in two: 
        list += l

print(list)