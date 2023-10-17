num=int(input())
if num//1000>=1 and (num%7==0 or num%17==0):
    print('yes')
else:
    print('no')