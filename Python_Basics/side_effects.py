emoticon ="v.v"

def main() :
    global emoticon # now we can modify the emoticon variable in 6th line and it modifies the global variable
    say("Is anyone there?")
    emoticon = ":D" # you can't change this without using global ----(var name)
    say("Oh,Hi!")

def say(phrase):
    print(phrase + " " + emoticon)

main()    

print(emoticon) # this here prints the modified global value 