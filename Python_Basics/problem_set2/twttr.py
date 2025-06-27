Input = input("Input : ")
print("output : " , end="")

for c in Input :
    if c not in ["A","E","I","O","U","a","e","i","o","u"] :
        print(c,end="")