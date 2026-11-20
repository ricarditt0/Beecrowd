n = int(input())

for _ in range(n):
    mine = input()
    stack = []
    diamonds = 0
    for char in mine:
        if char == "<":
            stack.append(char)
        elif char == ">":
            if stack:
                aux = stack.pop()
                if aux == "<":
                    diamonds += 1
                else:
                    stack.append(aux)
                    stack.append(char)
            else:
                stack.append(char)
    print(diamonds)