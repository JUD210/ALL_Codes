# You can call len() on any Python object that defines a .__len__() method:
class TheHobbit:
    def __len__(self):
        return 95022


the_hobbit = TheHobbit()
print(len(the_hobbit))
# 95022


# Note that the call to len() gives the return value of the .__len__() method. In fact, the implementation of len() is essentially equivalent to the following:
def len(obj):
    return obj.__len__()
