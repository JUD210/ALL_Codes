""" Documentation

Documentation is used to make your code easier to understand and use. Functions are especially readable because they often use documentation strings, or docstrings. Docstrings are a type of comment used to explain the purpose of a function, and how it should be used.

Here's a function for population density with a docstring.
"""

# Short Docstrings
def population_density1(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area


# Full Docstrings
def population_density2(population, land_area):
    """Calculate the population density of an area.

    INPUT:
        population: int. The population of that area
        land_area: int or float. This function is unit-agnostic, if you pass in values in terms of square km or square miles the function will return a density in those units.

    OUTPUT:
        population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area


# autoDocstring Extension's format
def population_density3(population, land_area):
    """Calculate the population density of an area.
    (This docstring format was created by autoDocstring)

    Arguments:
        population {int} -- The population of that area
        land_area {int or float} -- This function is unit-agnostic, if you pass in values in terms of square km or square miles the function will return a density in those units.

    Return:
        population_density {float} -- population / land_area. The population density of a particular area.
    """

    return population / land_area


# Compare these examples below.
print(population_density1(100, 5))
print(population_density2(100, 5))
print(population_density3(100, 5))
