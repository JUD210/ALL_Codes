""" Complex Boolean Expressions

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

if is_raining and is_sunny:
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")



    Good and Bad Examples

1. Don't use True or False as conditions

# Bad example
if True:
    print("This indented code will always get run.")

# Another bad example
if is_cold or not is_cold:
    print("This indented code will always get run.")


2. Be careful writing expressions that use logical operators

# Bad example
if weather == "snow" or "rain":
    print("Wear boots!")


3. Don't compare a boolean variable with == True or == False

# Bad example
if is_cold == True:
    print("The weather is cold!")

# Good example
if is_cold:
    print("The weather is cold!")

"""