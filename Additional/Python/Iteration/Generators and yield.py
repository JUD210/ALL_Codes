# https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/


t_list = [1, 2, "3", "4"]

print([x for x in t_list])
# [1, 2, '3', '4']
print(x for x in t_list)
# <generator object <genexpr> at 0x00000292FE0430C0>


def sim_gen_fuc(x):
    yield x + 1
    yield x + 10
    yield x + 100


""" Test Case 1 """
new_gen1 = sim_gen_fuc(0)

print(new_gen1)
# <generator object sim_gen_fuc at 0x000001C31BB31F48>
print(type(new_gen1))
# <class 'generator'>
print(list(new_gen1))
# [1, 10, 100]

for value in new_gen1:
    print(value)


""" Test Case 2 """
new_gen2 = sim_gen_fuc(0)

for value in new_gen2:
    print(value)
# 1
# 10
# 100

# print(next(new_gen1))
# Error: StopIteration


""" Test Case 3 """
new_gen3 = sim_gen_fuc(0)
print(next(new_gen3), next(new_gen3), next(new_gen3))
# 1 10 100

# print(next(new_gen3))
# Error: StopIteration

