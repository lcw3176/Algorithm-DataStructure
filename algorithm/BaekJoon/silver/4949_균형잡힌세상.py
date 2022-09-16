while True:
    s = input()
    stack = []

    if s == ".":
        break
    
    for i in s:
        if i == "(" or i == "[" or i == ")" or i == "]":
            stack.append(i)
        
        if len(stack) >= 2:
            close = stack.pop()
            open = stack.pop()

            if (open != "(" or close != ")") and (open != "[" or close != "]"):
                stack.append(open)
                stack.append(close)

    if len(stack) != 0:
        print("no")
    else:
        print("yes")