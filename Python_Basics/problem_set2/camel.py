def main():
    name = input("camelCase : ")

    for c in name :
        if(c.isupper()) :
            name = name.replace(c,'_'+c.lower())
    print(f"snake_case : {name}")

main()            

# print(c,end"") tells not to print endline after printing c