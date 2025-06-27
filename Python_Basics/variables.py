def get_guess(a):
    guess = a
    return guess

print(get_guess(6))

def get_guess1():
    guess = input() # this actually stores 50 as string not integer
    return guess

def get_guess2():
    guess = int(input("Enter a guess:")) #this int converts that in 
    return guess


def main():
    guess2 = get_guess2() # enter 50
    guess1 = get_guess1() #enter 50  

    if guess1 == 50 : # this is false as guess1 stores 50 as string and in rhs its 50 integer
        print("Guess 1 is an Integer!")
    elif  guess2 == 50 :
        print("Guess 2 is an Integer!")
    else :
        print("Incorrect!")

main()        
