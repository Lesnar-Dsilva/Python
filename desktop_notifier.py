import urllib.request,json
def getData(url):
    response = urllib.request.urlopen(url);
    if(response.getcode()==200):
        #reads the whole json file
        data = response.read()
        #makes json file readable
        jsonData = json.loads(data)
    else:print("Error occured", response.getcode())
    return jsonData
url = "https://hltv-api.vercel.app/api/news.json"
data = getData(url);
for i in data:
    print(i["title"]);
#5mins 21/05/2022