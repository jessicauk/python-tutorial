post = {
    "user_id": 209,
    "message": "D5 E5 C5 C4 G4",
    "language": "EN",
    "datetime": "20230215T124231Z",
    "location": (44.590533, -104.715556),
}

# Using constructor
post2 = dict(message="SS Cotopaxi", language="EN")
print(post2)

# Create key pirs
post2["user_id"] = 209
post2["datetime"] = "19771116T093001Z"
print(post2)

# Validation if exists a key in dictionary

if "location" in post2:
    print(post2["location"])
else:
    print("It does not exist")

# Try except block
try:
    print(post2["location"])
except KeyError:
    print("Post does not have location")

loc = post2.get("location", None) # If not then return None
print(loc)

#Iteration
for key, value in post2.items():
    print(key, "=", value)
