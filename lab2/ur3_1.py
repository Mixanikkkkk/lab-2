s=0
n=0
t = True
while t is True:
    hight=float(input('Введите рост ученика '))
    s+=hight
    n+=1
    answer=input("Остались ли ученики в классе? ")
    if answer.lower()=='нет':
        t=False
        print('Все ученики учтены')

print(f'Средний рост учеников:{(s/n):.2f}')