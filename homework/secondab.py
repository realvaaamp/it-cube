otwet=int(input())
a=otwet//1000
b=otwet%10
c=otwet//100%10
d=otwet//10%10
if a+b==c-d:
    print('да')
else:
    print('no')
