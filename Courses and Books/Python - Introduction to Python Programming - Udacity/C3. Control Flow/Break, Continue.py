""" Break, Continue
Sometimes we need more control over when a loop should end, or skip an iteration. In these cases, we use the break and continue keywords, which can be used in both for and while loops.

- break terminates a loop
- continue skips one iteration of a loop

Watch the video and experiment with the examples below to see how these can be helpful.
"""

# Loading Challenge

manifest = [("bananas", 15), ("mattresses", 24),
            ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]


# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\n=== Right METHOD ===")
weight = 0
limit = 100
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight == limit:
        print("  breaking from the loop now!")
        break
    elif weight > limit:
        print("  ERROR! Overloaded!")
        break
    elif weight + cargo_weight > limit:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

###

# the code breaks the loop when weight exceeds or reaches the limit
print("\n=== Wrong METHOD ===")
weight = 0
limit = 100
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= limit:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))