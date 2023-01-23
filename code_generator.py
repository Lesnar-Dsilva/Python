import string;
az = list(string.ascii_lowercase);
def a1z26_code(s):
    for x in az:
        for z in range(len(s)):
            if s[z] == x:s[z] = str(az.index(x)+1);
    return " ".join(s);

ascii = lambda s:" ".join([str(ord(x)) for x in s]);
def at(i):
    c = "";
    za = list(reversed(az));
    for q in i:
        if q == " ":c+= " ";
        else:
            for x in az:
                if x == q:c+=za[az.index(q)];
    return c;

def bin(s):
    bin_bytes = bytes(s,"ascii");
    return "".join(["{0:b}".format(x) for x in bin_bytes]);

def braille_code(s):
    t = str.maketrans(string.ascii_lowercase,"⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵");
    return s.translate(t);

def morse_code(s):
    c = "";
    morse = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."};
    for x in s:
        if x == " ":c+=" ";
        else:
            for z in morse.keys():
                if x == z:c+=morse[x];
    return c
user = "";
while user != "q":
    user = input("What encoding technqiue would you like to use?:\n1.a1z26\n2.ASCII\n3.Atbash\n4.Binary\n5.Braille\n6.Morse Code\nQ.To exit the program\n>")
    if user == "1":s = input("Enter a words or sentence: ").lower();print(a1z26_code(list(s)));
    elif user == "2":s = input("Enter a words or sentence: ").lower();print(ascii(list(s)));
    elif user == "3":i = input("Enter a words or sentence: ").lower();print(at(list(i)));
    elif user == "4":s = input("Enter a words or sentence: ").lower();print(bin(s));
    elif user == "5":s = input("Enter a words or sentence: ").lower();print(braille_code(s));
    elif user == "6":s = input("Enter a words or sentence: ").lower();print(morse_code(s));
    elif user == "q":print("Exiting...");
    else:print("Input not recognized.");
#2hrs 23/05/2022