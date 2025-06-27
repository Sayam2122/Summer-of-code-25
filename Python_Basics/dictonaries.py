def main():
    spacecraft = {"name" : "Voyager 1" , "distance" : 163}
    spacecraft["new key"] = "AU" # create or add a new key like this
    spacecraft.update({"orbit" : "Sun" , "game" : 5 }) #if we want to addd multiles keys together
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    =========Report=========

    Name : {spacecraft["name"]}
    Distance : {spacecraft["distance"]} {spacecraft["new key"]}
    Time : {spacecraft.get("time","Unknown")} 
    Orbit : {spacecraft.get("orbit" , "Unknown")}
    Game : {spacecraft.get("game" , "Unknown")}

#.get function check for that key if that key doesn't exit in our dictonary 
# then it prints the value we give in this case its unknown
I can also typr from this end because triple quotes denotes multiple line string
    ========================
    """
main()

distances = {
    "Voyager 1" : 163,
    "Voyager 2" : 136,
    "Pioneer 10" : 80  ,
    "New Horizons" : 58,
    "Pioneer 11": 44
}

for name in distances.keys():
    print(f"{name} is {distances[name]} AU from the Earth")
print()


def val():
    for value in distances.values():
        print( f"{value} AU is {convert(value)} m")    

def convert(au):
    return au*149597870700    

val()