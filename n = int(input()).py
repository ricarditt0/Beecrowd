n = int(input())
while n:
    bord = input()
    if bord.find('X.X')!= -1 or bord.find("XX.")!= -1 or bord.find(".XX")!= -1:
        print("S")
    elif bord.find('X') ==-1 and n%2 != 0:
        print("S")
    elif bord.find('X') ==-1 and n%2 == 0:
        print("N")
    elif bord.find('...') == -1:
        print("N")
    else:
        print("N")
        
    n = int(input())