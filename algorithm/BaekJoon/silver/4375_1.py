while True:
    try:
        x = int(input())
    except:
        break
    
    if x == 1:
        print(1)
        continue
    
    value = str()
    num = 2
    while True:
        value = "1" * num
        num += 1

        if int(value) % x == 0:
            print(len(value))
            break