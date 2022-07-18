captain = {
    "Enterprise":"Picard",
    "Voyagar":"Janeway",
    "Defiant":"Sissoko"
}

if  "Enterprise" in captain:
    print(captain["Enterprise"])
else:
    print("Unknown")

if  "Discovery" in captain:
    print(captain["Discovery"])
else:
    print("Unknown")

for ship, captained in captain.items():
    print(f'The {ship} is captained by {captained}')