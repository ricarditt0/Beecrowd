while True:
    try:
        expressao = input()
    except EOFError:
        break

    stack = []

    for ope in expressao:
        if ope == "(":
            stack.append(ope)
        elif ope == ")":
            if stack:
                aux = stack.pop()
                if aux == ")":
                    stack.append(aux)
                    stack.append(ope)
            else:
                stack.append(ope)
    print("correct" if not stack else "incorrect")
            