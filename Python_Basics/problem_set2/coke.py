Amount = 50

while Amount > 0:
    print(f"Amount Due : {Amount}")
    insert = int(input("Insert Coin : "))

    if insert in [25, 10, 5]: 
        Amount = Amount - insert

print(f"Change Owed : {abs(Amount)}")