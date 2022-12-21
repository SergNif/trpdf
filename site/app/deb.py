import math
import numpy as np
g = 0
h = 'll'
hj = []
print('Введите значени а =')
k=float(input())
print('Введите начало и конец промежутка')
a=input('Начало = ')
a=float(a)
b=input('Конец = ')
b=float(b)
print('y принадлежит от ',a,' до ',b)
y=input('Введите значение дельта y ')
y=float(y)
m=float((b-a)/k)+1
n=3*m
n=int(n)
m=int(m)
B= np.arange(n).reshape(m,3)
B = B.astype("float")
for i in range(0,m):
    B[i][0]=a+(i*k)
for c in range(0,m):
    B[c][1]=float(B[c][1])
    B[c][1]=(float)((2**(1-B[c][0]))-(2.5*math.cos(k)))
for z in range(0,m):
    B[z][2]=float(B[z][2])
    B[z][2]=(float)((math.log((math.fabs(B[z][0]-1)),10))+(B[z][1])**2)
print('Значение y      Значение x     Значение w ')
print(B)
# for n in range(0,50):
#     hj.append(n)
#     print(f'{n=}')

(72.0, 240.1898193359375, 76.9813003540039, 254.72525024414062)
(86.94390106201172, 240.1898193359375, 141.04080200195312, 254.72525024414062)
(535.01904296875, 240.1898193359375, 540.0003662109375, 254.72525024414062)