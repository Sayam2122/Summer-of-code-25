results = ["Mario" ,"Luigi"]

results.append("Princess Peach")
results.append("Yoshi")
results.append(["Koopa Troopa" , "Toad"])
results.extend(["Bowser","Donkey King Jr."])
results.remove("Luigi")
print(results)

results.reverse()
results.insert(3,"Luigi")
print(results)