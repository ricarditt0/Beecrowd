r,l = map(int,input().split())

PI=3.1415

volume = (4/3)*PI*(r**3)
quantity = l//volume
print(int(quantity))