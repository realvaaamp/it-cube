#ферзь
x1,y1,x2,y2=int(input()),int(input()),int(input()),int(input())
if abs(x1-x2)==abs(y1-y2) or abs(x2)!=abs(x1) and abs(y1)==abs(y2) or abs(x2)==abs(x1) and abs(y1)!=abs(y2):
    print('YES')
else:
    print('NO')