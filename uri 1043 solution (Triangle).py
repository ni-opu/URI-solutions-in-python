#for python 3.6 or above
[x,y,z] = map(float, input("type three number: ").split())
if x+y>z and y+z>x and z+x>y:
  print(f'Perimetro = {x+y+z}')
else:
  print(f'Area = {((x+y)/2)*z}')
  
#for python 3.4
[x,y,z] = map(float, input().split())
if x+y>z and y+z>x and z+x>y:
    result=x+y+z
    print('Perimetro =', result)
else:
    result=((x+y)/2)*z
    print('Area =', result)
