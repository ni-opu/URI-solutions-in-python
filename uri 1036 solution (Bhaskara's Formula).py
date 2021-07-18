A,B,C=map(float,input().split())
d=(B**2)-(4*A*C)
r=d**.5
if d<0 or A==0:
    print('Impossivel calcular')
else:
    e=(-B+r)/(2*A)
    f=(-B-r)/(2*A)
    print('R1 = %.5f'%e)
    print('R2 = %.5f'%f)
