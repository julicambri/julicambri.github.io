#request user input
user_numin = input("Please enter a number: ")
#request user choice
user_choice = input("Choose a base for conversion - 8 or 16: ")
#convert user input to hex
if user_choice == "8":
    print(hex(int(user_numin)))
#convert user input to octal
elif user_choice == "16":
    print(oct(int(user_numin)))