Items={}

while True:
    try :
        item = input().upper()

        Items[item] = Items.get(item, 0) + 1

        # if item not in Items:
        #     Items[item] = 1
        # else:
        #     Items[item] +=1 
    except EOFError:
        for ite in Items:
            print(f"{Items[ite]}  {ite}")
        break    
                