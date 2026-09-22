world_1 = str(input())
world_2 = str(input())
world_3 = str(input())

if (world_1 == "vertebrado"):
    if (world_2 == "ave"):
        if (world_3 == "carnivoro"):
            print("aguia")
        elif (world_3 == "onivoro"):
            print("pomba")
    elif (world_2 == "mamifero"):
        if (world_3 == "onivoro"):
            print("homem")
        elif (world_3 == "herbivoro"):
            print("vaca")
elif (world_1 == "invertebrado"):
    if (world_2 == "inseto"):
        if (world_3 == "hematofago"):
            print("pulga")
        elif (world_3 == "herbivoro"):
            print("lagarta")
    elif (world_2 == "anelideo"):
        if (world_3 == "hematofago"):
            print("sanguessuga")
        elif (world_3 == "onivoro"):
            print("minhoca")