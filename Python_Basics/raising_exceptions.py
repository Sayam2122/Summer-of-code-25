def main():
    pace = get_pace(26.4,10)
    print(f"You need to run each mile in {round(pace,2)} minutes.")

def get_pace(miles,minutes):
    if not minutes > 0 :
        raise ValueError ("Minutes must be greater than 0.")
    # if we don't know what kind of exeption we are raising , we can simply write raise Exception.
    
    return (minutes/miles)
main()        