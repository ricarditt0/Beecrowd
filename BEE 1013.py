
def maiorAB(a,b):
    return (a + b + abs(a-b))//2

a,b,c = map(int,input().split())
print(maiorAB(maiorAB(a,b),c),"eh o maior")