#solution of uri onlinejudge problem no.1038 (Snack)
x,y=map(int,input().split())
if x==1:
    v=4.00*y
elif x==2:
    v=4.50*y
elif x==3:
    v=5.00*y
elif x==4:
    v=2.00*y
elif x==5:
    v=1.50*y
print('Total: R$ %.2f'%v)
