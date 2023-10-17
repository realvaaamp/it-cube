a,b,c,d=int(input()),int(input()),int(input()), int(input())
if abs(a-c)==abs(b-d) and abs(a-c)==1 and abs(b-d)==1 or (a==c and abs(b-d)==1) or (b==d and abs(a-c)==1):
    print('yes')
else:
    print('no')
