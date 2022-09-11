while True:
    try:
        n = int(input())
    except:
        break

    num1 = 1
    digit = 1

    while True:
        if num1 % n == 0:
            print(digit)
            break
        else:
            digit += 1
            num1 = num1 * 10 + 1
