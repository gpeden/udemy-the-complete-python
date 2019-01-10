import json

file = open("friends.json", "r")
file_contents = json.load(file)
file.close()

print(file_contents['friends'][0])

dump = open("dump.json", "w")
dump.close()
