expression = input("Expression: ").strip()

count = 0

for text in expression:
    if text == " ":
        break
    else:
        count+=1
        
x = float(expression[:count])     
y = expression[count+1]
z = float(expression[count+3:].strip())

if y =="+":
    print(f"{(x+z):.1f}")
elif y =="-":
    print(f"{(x-z):.1f}")    
elif y=="/" and z != 0 :
    print(f"{(x/z):.1f}")
else:
    print(f"{(x*z):.1f}")        
