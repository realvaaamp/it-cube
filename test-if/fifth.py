#проверка условий
a=int(input('Введите число '))
if a%2==1:
    print("YES")
if 6<=a<=20 and a%2==0:
    print('YES')
if  2<=a<=5 and  a%2==0:
    print('NO')
if  20<a and a%2==0:
    print('NO')