h1,m1,h2,m2 = list(map(int, input().split()))
if h2>h1 or (h2==h1 and m2>m1):

    h = h2-h1
else:
    h = (h2-h1)+24
    
if m2<m1:
    h -= 1
    m = (m2-m1)+60
else:
    m = m2-m1

print('O JOGO DUROU ',h,' HORA(S) E ', m,' MINUTO(S)', sep='',end='\n')
