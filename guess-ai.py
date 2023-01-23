import random;
g = 0;
while g < 5:
    print("The computer will guess of a number from 1 to 10. Enter \"y\" if it's guess is correct or \"n\" for an incorrect guess, and the computer only has 5 guesses.")
    r = random.randint(1,10);
    ai = input(f"Is the random number {r}: ").lower();
    if ai == "y":
        print("The computer guessed correctly.")
        break;
    else:
        print("The computer guessed incorrectly, it will try again.\n")
        g+=1
print("The computer didn't get any guesses correct, you can play again, if you like.") if g == 5 else None;
#20mins 08/05/2022