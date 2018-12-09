# https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/

"""
TODO: Learn more
FIXME: 
"""

def sim_gen_fuc(x):
    yield x + 1
    yield x + 10
    yield x + 100


num = 0
new_gen1 = sim_gen_fuc(num)

print(new_gen1)
# <generator object sim_gen_fuc at 0x000001C31BB31F48>
print(type(new_gen1))
# <class 'generator'>


for value in new_gen1:
    print(value)
# 1
# 10
# 100

# print(next(new_gen1))
# Error: StopIteration


new_gen2 = sim_gen_fuc(num)

print(next(new_gen2), next(new_gen2), next(new_gen2))
# 1 10 100

# print(next(new_gen2))
# Error: StopIteration
