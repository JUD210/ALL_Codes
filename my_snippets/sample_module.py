def python_intro_path(Chapter):
    if Chapter.lower() == "c1":
        return "CS Study Note/[Python] Introduction to Python Programming (Udacity)/C1. Data Types and Operators/"
    elif Chapter.lower() == "c2":
        return "CS Study Note/[Python] Introduction to Python Programming (Udacity)/C2. Data Structures/"
    elif Chapter.lower() == "c3":
        return "CS Study Note/[Python] Introduction to Python Programming (Udacity)/C3. Control Flow/"
    elif Chapter.lower() == "c4":
        return "CS Study Note/[Python] Introduction to Python Programming (Udacity)/C4. Functions/"
    elif Chapter.lower() == "c5":
        return "CS Study Note/[Python] Introduction to Python Programming (Udacity)/C5. Scripting/"
    else:
        raise Exception("Your argument is not 'C1 ~ C5'")


print(python_intro_path(input()))
