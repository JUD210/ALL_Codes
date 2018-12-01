""" 
Used to "iterate", or do something repeatedly, over an iterable.
"""


cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

""" Creating Lists """

capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
print(capitalized_cities)


""" Modifying Lists """
print("")

for index in range(len(cities)):
    cities[index] = cities[index].title()
print(cities)


""" Don't Mistake! """
print("\n=== Don't Mistake!")

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)
# The printed output for the names list will look exactly like it did in the first line
