n = int(input())
term1=0
term3=0
for i in range(n):
     x = float(input(f'Координата X точки {i+1}: '))
     y = float(input(f'Координата Y точки {i+1}: '))
     if x>0:
         if y>0:
             term1+=1
             print("точка лежит в 1 четверти")
         if y<0:
             print("точка лежит в 4 четверти")
     if x<0:
         if y>0:
             print("точка лежит во 2 четверти")
         if y<0:
             print("точка лежит в 3 четверти")
             term3+=1
     print()

print(f'1 четверть: {term1}\n3 четверть: {term3}')