import random;
r = int(input("Enter a random number: "));
g = random.sample(range(0,100,2),50);
b = 0;
while b != r:
    if r in g[:(len(g)//2)]:
        g = g[:(len(g)//2)];
    elif r in g[(len(g)//2):]:
        g = g[(len(g)//2):];
    else:
        g = g[:(len(g)//2)];
        if len(g) == 0:
            print("Size: 0, input not found.");
            break;
    if g[0] == r and len(g) == 1:
        b = r;
        print(r,"Found!");
#35mins 19/05/2022