import random

subjects = [
    "Akhil",
    "Virat Kohli",
    "Shahrukh Khan",
    "A group of monkeys",
    "Prime Minister Modi",
    "Driver",
    "Dog",
    "My neighbor's goldfish",
    "A confused alien",
    "A lazy superhero",
    "A talking parrot",
    "My strict math teacher",
    "An overacting news reporter",
    "A secret ninja uncle"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "declares war on",
    "orders",
    "accidentally marries",
    "challenges to a rap battle",
    "starts a podcast with",
    "throws chappal at",
    "opens a startup with",
    "steals WiFi from",
    "writes a love letter to",
    "does bhangra with"
]

place_or_things = [
    "at Red Fort",
    "in a Mumbai local train",
    "inside parliament",
    "at Ganga Ghat",
    "in my home",
    "a plate of samosas",
    "on the moon",
    "inside a PUBG lobby",
    "during an IPL match",
    "in a secret underground bunker",
    "at a wedding buffet",
    "on Instagram live",
    "in a coding interview",
    "at a chai tapri"
]

while True:
    name = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)

    headline = f"🚨 BREAKING NEWS: {name} {action} {place_or_thing}!"
    print("\n" + headline)

    userInput = input("\nDo you want another headline? (yes/no): ").strip().lower()

    if userInput == 'yes':
        continue
    elif userInput == 'no':
        print("\n😂 Thanks for watching Fake News Channel 24x7!")
        break
    else:
        print("\n⚠️ Please type only 'yes' or 'no'.")