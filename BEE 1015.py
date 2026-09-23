from math import sqrt

xi,yi = map(float,input().split())
xf,yf = map(float,input().split())
distance = sqrt((xi-xf)**2 + (yi-yf)**2)
print(f"{distance:.4f}")