def main():
    
    difficulty = input("Difficult or Casual ??").strip()
    if not (difficulty == "Difficult" or difficulty == "Casual") :
        print("Enter a valid difficullty")
        return
    
    players = input("Multiplayer or Single-Player ??").strip()
    if not (players == "Multiplayer" or players == "Single-Player") :
        print("Enter a valid players")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
            recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-Player":
            recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer" :
            recommend("Hearts")
    else :
            recommend("Clock")


def recommend(game):
    print("The game you like is:",game)

main()                