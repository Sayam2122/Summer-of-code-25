#list words as stack (LIFO)
def main():
    History=[]

    while True:
        action = input("Action : " )

        if action == "Undo":
            undone = History.pop() # as lifo it removes and last added element
            print(f"Undone :{undone}")
        elif action == "Restart":
            History.clear()    
        else :
            History.append(action)
        print(History)        

main()        