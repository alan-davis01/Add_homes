m = int(input('Введите число_1: '))
n = int(input('Введите число_2: '))
x = range(m,n)
for i in x:
    for e in range(2,i-1):
        if i % e==0:
            print("Chislo",i, "Delite", e)
