s=0
n=0
t = True
while t is True:
    mark1 = int(input('1 оценка: '))
    mark2 = int(input('2 оценка: '))
    mark3 = int(input('3 оценка: '))
    mark4 = int(input('4 оценка: '))
    if mark1 != 2 and mark2 != 2 and mark3 != 2 and mark4 != 2:
        if mark1 != 3 and mark2 != 3 and mark3 != 3 and mark4 != 3:
            s += 1
    print()
    answer=input("Остались ли ученики в классе? ")
    if answer.lower()=='нет':
        t=False
        print('Все ученики учтены')

print(f'{s} ученика не получили 2 или 3')