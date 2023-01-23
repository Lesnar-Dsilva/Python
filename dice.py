import random;

i = "";
die = lambda:random.randint(1,6);

while i!="n":
    print(die());
    i = input("Would you like to roll again? (Y/N): ").lower();
#3mins 12/05/2022