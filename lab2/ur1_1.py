x=float(input())
y=float(input())
r=2
if abs(x**2+y**2-r**2)<=10**(-3):
    print('Лежит')
else:
    print('Не лежит')
