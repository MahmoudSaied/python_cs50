def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            # pass -- if you choose this then it will just igoner the error

            # to print an error message
            print("The value you entered is not an integer, please try again")
    

def main():
    x = get_int("Insert a value for y: ")
    print(x)

main()