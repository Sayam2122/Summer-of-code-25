WORDS ={"HAIR" :4 , "PAIR":4,"CHAIR":5 ,"GRAPHIC" : 7}

def main():
    print("Welcome to Spelling Bee!!")
    print("Your letters are : A I P G H C R")

    for word,points in WORDS.items():
        print(f"{word} was worth {points} points.")

    while len(WORDS) > 0:

        print (f"{len(WORDS)} words left!")
        guess = input("Guess a word : ").strip().upper()

        if guess == "GRAPHIC" :
            WORDS.clear() # or break
            print("You have Won!!")

        if guess in WORDS.keys() :
            Points =  WORDS.pop(guess)
            print(f"Good Job!You scored {Points} points.")

    print("That's the game!")

main()