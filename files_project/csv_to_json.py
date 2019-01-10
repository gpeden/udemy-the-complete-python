# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
import json

json_list = []

with open("cvs_file.txt", "r") as file:
    for line in file.readlines():
        club, city, country = line.strip().split(',')
        data = {
            'club': club,
            'city': city,
            'country': country
        }
        json_list.append(data)


with open("json_file.txt", "w") as outfile:
    json.dump(json_list, outfile)



