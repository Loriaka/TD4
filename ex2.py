import requests
r=requests.get("https://opendomesday.org/api/1.0/county/")
for i in r.json() :
        if i["name"]=="Derbyshire":
                    for j in i["places_in_county"]:
                                    print(j["id"])
