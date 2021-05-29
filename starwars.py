import requests

maim_api="https://swapi.dev/api/"
resources=requests.get("https://swapi.dev/api/").json()
print("START WARS\n")
print(resources['people'])
print(resources['planets'])
print(resources['films'])

while True:
    search=input("Define a resource withing the platform: ")
    if search == "quit" or search == "q":
        break
    elif search == "starships":
        print("Choose a value ID from 0 to 36")
        search2=input("Choose ID: ")
        url=maim_api+search+"/?search="+search2
        json_data=requests.get(url).json()
        #print(json_data)
        print("Resource count: ",json_data["count"])
        print("Resource name: ",json_data["results"][0]["name"])
        movies=json_data["results"][0]["films"][0:6]
        for i in movies [0:6]:
            print(i)
    elif search == "people":
        url=maim_api+search+"/?search="
        json_data=requests.get(url).json()
        #print(json_data)
        print("Resources count: ",json_data["count"])
        for i in json_data["results"][0:36]:
            print("==============================================================")
            print("Name of character: ", i["name"], "|", "height: ", i["height"])
            print("Hair color: ", i["hair_color"], "|", "eye color: ", i["eye_color"])
            print("Birth Day: ", i["birth_year"], " | ", "Gender: ",i["gender"])
            print("==============================================================")
    elif search == "films":
        url=maim_api+search+"/?search="
        json_film = requests.get(url).json()
        #print(type(json_film))
        print("Resorce count: ",json_film["count"])
        for i in json_film["results"][0:6]:
            print(i)["title"]
    elif search == "species":
        url=maim_api+search
        url2=maim_api+search+"/?page=2"
        json_species=requests.get(url).json()
        print("Resource count: ", json_species["count"])
        for i in json_species["results"][0:10]:
            print(i["name"])
        json_species2=requests.get(url2).json()
        for i in json_species2["results"][0:10]:
            print(i["name"])
    elif search=="planets":
        url=maim_api+search+"/"
        json_planets = requests.get(url).json()
        for i in json_planets["results"][0:60]:
            print("--------------------------------------------------------------------------------")
            print("Name of the character: ", i["name"], " | ", "Rotation period: ",i["rotation_period"])
            print("Orbital period: ",i["orbital_period"], " | ", "Diameter: ",i["diameter"])
            print("Climate: ",i["climate"], " | ", "Terrain: ",i["terrain"])