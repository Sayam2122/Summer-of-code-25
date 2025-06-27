SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "the Proud family"
]
print()
def main():
    for show in SHOWS:
        print(show) 
    print()
main()

def capital():
    for show in SHOWS:
        print(show.capitalize()) 
    print()
capital()

def title():
    for show in SHOWS:
        print(show.title()) 
    print()
title()

def strip():
    for show in SHOWS:
        print(show.strip()) 
    print()
strip()

def strip_title():
    for show in SHOWS:
        print(show.strip().title()) 
    print()
strip_title()

def append_means():
    new_shows=[] # makes a new empty list
    for show in SHOWS:
        new_shows.append(show.strip().title()) # adding elements in new lists like printing one by one.
    print(new_shows)
    print()
    print('\n'.join(new_shows)) # this joins the list by a space bar as i have guven space between th colons.(and if i tye\n thenbn it will join by adding new line after every elemrn)
append_means()

