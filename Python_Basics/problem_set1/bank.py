output = input("Greeting: ").lower().strip()

if output.startswith("hello"):
    print("$0")
elif output.startswith("h"):
    print("$20")        
else :
    print("$100")

# chatgpt without startswith

""""
greeting = input("Greeting: ").strip().lower()

if greeting[:5] == "hello":
    print("$0")
elif greeting[:1] == "h":
    print("$20")
else:
    print("$100")
    
"""    
