#solution of uri onlinejudge problem no.1021 (banknotes and coins)
x=float(input())
z=x
a=z//100
z=z%100
b=z//50
z=z%50
c=z//20
z=z%20
d=z//10
z=z%10
e=z//5
z=z%5
f=z//2
g=z%2
z=int(x*100)
z=z%100
h=z//50
z=z%50
i=z//25
z=z%25
j=z//10
z=z%10
k=z//5
l=z%5
print('NOTAS:')
print('%d nota(s) de R$ 100.00'%a)
print('%d nota(s) de R$ 50.00'%b)
print('%d nota(s) de R$ 20.00'%c)
print('%d nota(s) de R$ 10.00'%d)
print('%d nota(s) de R$ 5.00'%e)
print('%d nota(s) de R$ 2.00'%f)
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00'%g)
print('%d moeda(s) de R$ 0.50'%h)
print('%d moeda(s) de R$ 0.25'%i)
print('%d moeda(s) de R$ 0.10'%j)
print('%d moeda(s) de R$ 0.05'%k)
print('%d moeda(s) de R$ 0.01'%l)
