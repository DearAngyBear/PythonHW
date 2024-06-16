import math
a = float(input("Введите сторону квадрата "))
def square (x):
     S = x*x
     return S
S = square (a)
print (math.ceil(S))
