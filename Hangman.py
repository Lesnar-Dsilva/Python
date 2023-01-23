import random;

words = ["abyss","avenue","azure","blitz","blizzard","bookworm","crypt","cycle","duplex","equip","espionage","fixable","foxglove","funny","glyph","gizmo","haiku","hyphen","icebox","ivory","jackpot","jelly","khaki","kiosk","matrix","megahertz","nowadays","nightclub","onyx","oxygen","pixel","psyche","puzzling","quartz","queue","quiz","rickshaw","scratch","shiv","sphinx","strength","thumbscrew","transcript","vodka","vortex","voodoo","wavy","wave","whiskey","xylophone","yippee","yoked","zigzag","zipper"];
choice = random.choice(words);
guess = ["_" for x in choice];

#words are too long and words with "j"'s and "z"'s are being used which have a low probability of being guessed. Hence lives/guesses aren't being used.

while "".join(guess) != choice:
    i = input("Guess a letter in the word: ").lower();
    if i in choice and i != "":
        if i in guess:
            print("Letter has been guessed already.");
            print("".join(guess));
        else:
            for x in range(len(choice)):
                if choice[x] == i:
                    guess[x] = i;
            print("Letter found in word.");
            print("".join(guess));
    
    else:
        print("Letter not found in word.");

print("\n"+"".join(guess).upper()+", you guessed the whole word.");
#35mins 07/05/2022