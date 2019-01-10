# Ask the user for a list of 3 friends
friends = input('Enter three friends, seperated by commas: ').split(',')

print(f"Friends: {friends}")

# For each friend, we'll tell the user whether they are nearby (in people)
people_file = open("people.txt", "r")

people = [line.strip() for line in people_file.readlines()]
people_file.close()

print(f"People: {people}")

# For each friend, we'll save their name to 'nearby_friends.txt'
nearby_friends = set(people).intersection(set(friends))

print(nearby_friends)
print(f"People: {people}")

nearby_file = open("nearby_friends.txt", "w")

for friend in nearby_friends:
    print(f"{friend} is a nearby! Meetup with them.")
    nearby_file.write(f"{friend}\n")

nearby_file.close()
