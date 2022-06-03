a,b=map(int, input().split())
if a==b:
    print('O JOGO DUROU 24 HORA(S)')
elif a<b:
    t=b-a
    print('O JOGO DUROU %d HORA(S)' %t)
elif a>b:
    t=(24-a)+b
    print('O JOGO DUROU %d HORA(S)' %t)
elif a!=0 and b==0:
    t=24-a
    print('O JOGO DUROU %d HORA(S)' %t)
