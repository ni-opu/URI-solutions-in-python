#solution of uri onlinejudge problem no.1040 (Average 3)
a,b,c,d = map(float,input().split())
average = (a*2+b*3+c*4+d*1)/10
print('Media: %.1f' %average)
if average >= 7.0:
    print('Aluno aprovado.')
elif average < 5.0:
    print('Aluno reprovado.')
elif average >= 5.0 and average <= 6.9:
    print('Aluno em exame.')
    x = float(input())
    print('Nota do exame: %.1f' %x)
    final_avg = (x+average)/2
    if final_avg >= 5.0:
        print('Aluno aprovado.')
        print('Media final: %.1f' %final_avg)
    else:
        print('Aluno reprovado.')
        print('Media final: %.1f' %final_avg)
