import pandas as pd

df = pd.read_csv("habitable_stars.csv")

name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
distance = df["Distance"].to_list()
gravity = df["Gravity"].to_list()


final_stars = []

temp_dictionary ={}
for header in range(0,len(name)):
    temp_dictionary["name"]=name[header]
    temp_dictionary["mass"]=mass[header]
    temp_dictionary["radius"]=radius[header]
    temp_dictionary["distance"]=distance[header]
    temp_dictionary["gravity"]= gravity[header]
    final_stars.append(temp_dictionary)
    temp_dictionary ={}
print(final_stars)