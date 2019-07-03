"""
You're allowed to annotate a variable without giving it a value. This adds the annotation to the __annotations__ dictionary, while the variable remains undefined:

>>> nothing: str
>>> nothing
NameError: name 'nothing' is not defined

>>> __annotations__
{'nothing': <class 'str'>}
Since no value was assigned to nothing, the name nothing is not yet defined.

"""
