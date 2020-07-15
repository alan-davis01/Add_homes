# n = 3 #список в списке
# l = []
# for i in range(n):
#     l.append(
#             list(range(0, n))
#     )
# print(l)
# import random
# n = 3 #со случайными числами через рандом
# l = []
# for i in range(n):
#     vloz_spisok = []
#     for j in range(n):
#         vloz_spisok.append(
#             random.randint(0,9)
#         )
#         l.append(vloz_spisok)
# print(l)

# import random
# n = 3 #со случайными числами через рандом (найти сумму)
# l = []
# for i in range(n):
#     vloz_spisok = []
#     for j in range(n):
#         vloz_spisok.append(
#             random.randint(0,9)
#         )
#         l.append(vloz_spisok)
#         print(l)
#         summa = 0
# for i in l:
#     for j in i:
#         if j % 3 ==0:
#             summa +=j
# print(summa)

# import random
# n = 3 #определить сколько раз встречется число 7 среди элементов
# l = []
# for i in range(n):
#     vloz_spisok = []
#     for j in range(n):
#         vloz_spisok.append(
#             random.randint(0,9)
#         )
#         l.append(vloz_spisok)
#         summa = 0
# for i in l:
#     for j in i:
#         if j==7:
#             summa +=1
# print(summa)

#присвоение буквы к индексу
# for i, elem in enumerate (['a', 'b', 'c', 'd']):
#     print(f'{i}-{elem}')

#задание 5.04

# import random
#
# n = 3
# m = 3
# l = []
# for i in range(n):
#     stroka = []
#     for j in range (m):
#         stroka.append(random.randint(0,9))
#     l.append(stroka)
#     summa = 0
# for i in l:
#     for j in i:
#          summa +=j #найти сумму
# print(summa)
#
# sred_znachenie = summa/ (n*m) #среднее значение
# print(sred_znachenie)
#
# counter = 0 #найти больше среднего значения
# for i in l:
#     for j in i:
#         if j > sred_znachenie:
#             counter+=1
# print(counter)

# s = 'sama' #что бы узнать, правда ли слово начинается с буквы s
# print(
#     s.startswith('s')
# )

pupils = [{
    'firstname': 'Masha',
    'Group': 42,
    'physics': 7,
    'informatics': 6,
    'history': 8,
},{
    'firstname': 'Ira',
    'Group': 42,
    'physics': 7,
    'informatics': 6,
    'history': 8,
}]

for pupil in pupils:
    summa = 0
    counter = 0
    for key not in pupil.keys():
        if key not in ["firstname", "Group"]:
            summa += pupil[key]
            counter += 1
        if summa/counter >4:
            print(pupil)



