user = "";
while user != "q":
    user = input("Enter your expression (remember to use parentheses \"()\" to get accurate results) or Q to quit the program\n> ");
    try:
        print(eval(user));
    except:
        print("\nENTER AN EXPRESSION.\n");
#5mins 25/05/2022