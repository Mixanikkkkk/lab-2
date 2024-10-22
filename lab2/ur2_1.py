n=int(input())
s=0
for i in range(n):
    hight=float(input())
    s+=hight
print(f'Средний рост учеников:{s/n}')