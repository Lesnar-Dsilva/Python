import random,string;

l = input("What length should the password be?: ");
symbols = "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/";
c = [1,2,3,4,5,6,7,8,9,0];
c.extend(list(string.ascii_letters)),c.extend(list(symbols));
p = "";

for x in range(int(l)):
    p += str(random.choice(c));

print("Password generated:",p)
#10mins 07/05/2022