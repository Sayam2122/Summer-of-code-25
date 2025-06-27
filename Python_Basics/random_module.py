import random

cards = ["Jack","Queen", "King"]

def main():
    # A seed is something that is changed and decided by the runtime of our system 
    # but we can fix that such that got same random output for same seed

    random.seed(4)

    print(random.choice(cards))
    print(random.choices(cards,k=2))
    # In ths a problem that both can also be same
    # In this happens with replacement picks one card then put it back then choose another one

    print(random.sample(cards,k=2))
    # This happens without replacement picks one then keep that side 

    print(random.choices(cards,weights=[50,30,20],k=2))
    
main()    
