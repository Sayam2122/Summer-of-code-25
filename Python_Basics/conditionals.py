def main():
    difficulty = input("Difficult or Casual ??").strip()
    players = input("Multiplayer or Single-Player ??").strip()

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        else:
            recommend("Klondike")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        else:
            recommend("Clock")
    else :
        print("Enter a valid difficullty")

def recommend(game):
    print("The game you like is:",game)

main()                