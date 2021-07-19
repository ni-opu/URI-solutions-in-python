#solution of uri onlinejudge problem no.1038 (Snack)
#with for loop::(faster)
x,y=map(int,input().split())
v={1:4.00,2:4.50,3:5.00,4:2.00,5:1.50}
for i in v:
    if x==i:
        p=v[i]*y
print('Total: R$ %.2f'%p)

#with if condition::
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
