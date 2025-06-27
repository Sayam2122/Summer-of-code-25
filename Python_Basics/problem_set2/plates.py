# s = "Hello"
# if s.isalpha():
#     print("Only alphabets")

# s = "12345"
# if s.isdigit():
#     print("Only digits")

# s = "abc123"
# if s.isalnum():
#     print("Alphanumeric")


def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (1 < len(s) < 7) :
        return False
    elif not s.isalnum():
        return False
    elif not s[:2].isalpha():
        return False
    else :
        for i in range(len(s)):
            if s[i].isdigit():
                if s[i] == '0' or not s[i+1:].isdigit() :
                    return False
                break
                
    return True


main()