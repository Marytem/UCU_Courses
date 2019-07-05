import math

r = eval(input()) 
x = math.pi
V = 4/3 * x * r ** 3
A = 4 * x * r ** 2 

if round(V,3) == round(V):
    print ('V = ', int(round(V)))
else:
    print('V = ', round(V,3))
if round(A,3) == round(A):
    print ('A = ', int(round(A)))
else:
    print('A = ', round(A,3))