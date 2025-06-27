months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date : ")

        if date[0].isdigit():
            date = date.split("/")

            if not len(date) == 3:
                raise ValueError()
            
            if int(date[1]) > 31:
                raise ValueError()
            
            print(f"{date[2]}-{date[0]}-{date[1]}")
            
        else :
            date = date.split(" ")
    except ValueError:
        continue             