n=int(input('напишите число от 1 до 9 '))
if 1<=n<=9:
    sum=n+int(str(n)*2)+int(str(n)*3)
    print(sum)
else:
    print('не подходит')