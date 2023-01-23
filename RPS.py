#Rock, paper, scissors
import random;
bo,ai,u,rps = 3,0,0,["rock","paper","scissors"];
while bo > 0:
    a,y = random.choice(rps),rps[int(input("1 = Rock, 2 = Paper and 3 = Scissors: "))-1]

    if (y == "rock" and a == "scissors") or (y == "scissors" and a == "paper") or (y == "paper" and a == "rock"):
        u+=1;
        bo-=1;
    elif y==a:print("Tie!");
    else:
        ai+=1;
        bo-=1;

    print("AI-"+a.capitalize()+" USER-"+y.capitalize());
    print(f"AI {ai}:YOU {u}");

print("User WINS!") if u > ai else print("AI WINS!");
#30mins 06/05/2022