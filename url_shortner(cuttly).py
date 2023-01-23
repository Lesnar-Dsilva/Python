import requests
key = "9c87439bb5d616d84ddc05d416e7866ffb3e7";
#"https://" REQUIRED
url = "https://www.google.com";
api = f"https://cutt.ly/api/api.php?key={key}&short={url}";
data = requests.get(api).json()["url"];
print("Shortened URL:",data["shortLink"]);