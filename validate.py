email = input("What's your email? ").strip()

try:
    user_name, domain = email.split("@")
    if len(user_name) > 0 and "." in domain:
        print("Valid")
    else:
        print("Invalid")
except ValueError:
    print("Not Valid")