n = int(input())
r1=float(input())
r2=float(input())
popadaet=0
for i in range(n):
     x = float(input(f'Координата X точки {i+1}: '))
     y = float(input(f'Координата Y точки {i+1}: '))
     print()
     if x**2+y**2>=r1**2 and x**2+y**2<=r2**2:
         popadaet+=1
print(f'Попадает: {popadaet}\nНе попадает: {n-popadaet}')

