def doc_string():
    """
    Docstrings help document python functions
    This is the docstring associated with this function
    """
    return "I have a docstring"


print(doc_string())
# I have a docstring

print(doc_string.__name__)
# doc_string

print(doc_string.__doc__)
#
#    Docstrings help document python functions
#    This is the docstring associated with this function
#
help(doc_string)
#
#    Docstrings help document python functions
#    This is the docstring associated with this function
#


def uppercase(f):
    """
    I am uppercase
    """

    def f_wrapper():
        """
        I am uppercase wrapper
        """

        return f().upper()

    return f_wrapper


@uppercase
def doc_string_uppercased():
    """
    Docstrings help document python functions
    This is the docstring associated with this function
    """
    return "I have a docstring"


print(doc_string_uppercased())
# I HAVE A DOCSTRING

print(doc_string_uppercased.__name__)
# f_wrapper

print(doc_string_uppercased.__doc__)
#
#         I am uppercase wrapper
#
help(doc_string_uppercased)
#
#         I am uppercase wrapper
#
