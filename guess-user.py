import random;
t = 0;
while t < 25:
    t+=1;
    x = random.randint(1,10);
    y = int(input("Enter an integer between 1 and 10 inclusively: "));
    if y > x:
        print("Too high!");
    elif y < x:
        print("Too low!");
    else:
        print("You guessed correctly!");
        break;
#5mins 06/05/2022