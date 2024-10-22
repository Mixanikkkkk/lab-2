n = int(input())
s=0
for i in range(n):
    mark1 = int(input('1 оценка: '))
    mark2 = int(input('2 оценка: '))
    mark3 = int(input('3 оценка: '))
    mark4 = int(input('4 оценка: '))
    if mark1!=2 and mark2!=2 and mark3!=2 and mark4!=2:
        if mark1 != 3 and mark2 != 3 and mark3 != 3 and mark4 != 3:
            s+=1
    print()
print(f'{s} ученика не получили 2 или 3')