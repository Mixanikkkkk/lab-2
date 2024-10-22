r1=float(input())
r2=float(input())
popadaet = 0
n=0
t = True
while t is True:
    x = float(input(f'Координата X точки {n + 1}: '))
    y = float(input(f'Координата Y точки {n + 1}: '))
    print()
    n+=1
    if x ** 2 + y ** 2 >= r1 ** 2 and x ** 2 + y ** 2 <= r2 ** 2:
        popadaet += 1
    answer = input("Остались ли точки? ")

    if answer.lower()=='нет':
        t=False
        print('Все точки учтены')

print(f'Попадает: {popadaet}\nНе попадает: {n - popadaet}')