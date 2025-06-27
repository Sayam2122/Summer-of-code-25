def main():
    time = convert(input("What time is it? ").strip())
    if 7<= time <=8 :
        print("breakfast time")
    elif 12<= time <=13 :
        print("lunch time")
    elif 18<= time <=19 :
        print("dinner time")  


def convert(time):
    back = float(time[-2:])/60
    front = float(time[:-3])
    return(front+back)

# def convert(time):
#     hours, minutes = time.split(":")      # split "7:30" into ["7", "30"]
#     return float(hours) + float(minutes) / 60


if __name__ == "__main__": 
    main()

# In Python, every file has a built-in variable called __name__

# If the file is run directly (e.g., python myfile.py), then:
#     __name__ == "__main__"
#     => This means the file is the main program.

# If the file is imported into another file (e.g., import myfile), then:
#     __name__ == "myfile"
#     => This means it's being used as a module.

# So we use this to control what runs:
#     if __name__ == "__main__":
#         main()

# This ensures main() runs only when the file is executed directly,
# not when it's imported somewhere else.
