import requests;
username,password = "o_6ifbgsr1v5","GamingGeek1";
#access token
a = requests.post("https://api-ssl.bitly.com/oauth/access_token",auth=(username,password));
if a.status_code == 200:
    access = a.content.decode();
    print("Acess granted: ",access);
else:
    print("Access denied, exiting...");
    exit();
#request headers
head = {"Authorization":f"Bearer {access}"};
g = requests.get("https://api-ssl.bitly.com/v4/groups",headers=head);
if g.status_code == 200:
    groups = g.json()["groups"][0];
    guid = groups["guid"];
else:
    print("Cannot get GUID, exiting...")
    exit();
#url shortner
url = "https://www.google.com";
short = requests.post("https://api-ssl.bitly.com/v4/shorten",json={"group_guid":guid,"long_url":url},headers=head);
if short.status_code == 200:
    link = short.json().get("link");
    print("Shortened URL:",link);