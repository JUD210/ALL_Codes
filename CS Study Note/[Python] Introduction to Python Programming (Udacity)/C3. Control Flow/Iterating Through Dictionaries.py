cast = {
    "Jerry Seinfeld": "Jerry Seinfeld",
    "Julia Louis-Dreyfus": "Elaine Benes",
    "Jason Alexander": "George Costanza",
    "Michael Richards": "Cosmo Kramer"
}


for key in cast:
    print(key)

print("")

for key, value in cast.items():
    print("Actor: {}    \tRole: {}".format(key, value))