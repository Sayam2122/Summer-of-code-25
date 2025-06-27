def main():
    dollars = dollars_to_float(input("How much was the meal? ").strip())
    percent = percent_to_float(input("What percentage would you like to tip? ").strip())
    tip = dollars * percent
    print(f"Leave ${tip:.2f}") # this f here allows to take inner bracket as a varile and do the function like
# .2f truncate after 2 decimal places and without using f this will simple print Leave ${tip:.2f}.

def dollars_to_float(d):
    return(float(d[1:]))

def percent_to_float(p):
    return(float(p[:-1])/100)

main()