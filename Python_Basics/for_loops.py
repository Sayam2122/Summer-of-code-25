def main():
    names = ["Mario" , "Yoshi" , "Luigi" ,"Daisy"]

    for name in names :
        print(write_letter(name,"Princess  Peach"))

    for i in range(len(names)):
        print(write_letter(names[i],"Princess Peach"))    

def write_letter(receiver,sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},

        You are cordially invited to a ball at    
        Peach's Castle this eveninig , 7 PM.

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

main()
