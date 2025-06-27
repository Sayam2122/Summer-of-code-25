while True :
    try :
        Input = input("Fraction : ")

        for i in range(len(Input)):
            if Input[i] == "/":
                x = int(Input[:i])
                y = int(Input[(i+1):])
                break
    # x, y = map(int, input("Fraction: ").split("/"))   
        if x > y :
            continue
        percent = round((x/y)*100)
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else :
            print(f"{percent}%")
    except (ValueError, ZeroDivisionError): 
        continue
    break

