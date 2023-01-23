email = input("Enter a email: ");
username = email.split("@")[0];
domain = email.split("@")[1].split(".")[0];
print("Username: "+username+"\n"+"Domain: "+domain);
#10mins 19/05/2022