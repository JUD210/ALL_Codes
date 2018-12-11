
elements = {'hydrogen': {'number': 1,
                         'weight': 1.00794,
                         'symbol': 'H'},
            'helium': {'number': 2,
                       'weight': 4.002602,
                       'symbol': 'He'}}

helium = elements['helium']
print(helium)
# {'number': 2, 'weight': 4.002602, 'symbol': 'He'}

hydrogen_weight = elements['hydrogen']['weight']
print(hydrogen_weight)
# 1.00794


# create a new oxygen dictionary
oxygen = {'number': 8, 'weight': 15.999, 'symbol': 'O'}

# assign 'oxygen' as a key to the elements dictionary
elements['oxygen'] = oxygen

# assign 'is_noble_gas' values to the `elements` dict
# The syntax for adding elements to nested data structures is about the same as it is for reading from them.

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
elements['oxygen']['is_noble_gas'] = 'Not Sure'

print('elements = ', elements)
# elements =  {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H', 'is_noble_gas': False}, 'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He', 'is_noble_gas': True}, 'oxygen': {'number': 8, 'weight': 15.999, 'symbol': 'O', 'is_noble_gas': 'Not Sure'}}

"""
TODO: Find a way how to print like below.

# elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
#             'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'},
#             'oxygen': {'number': 8, 'weight': 15.999, 'symbol': 'O'}}
"""

print("\n".join(elements))
# hydrogen
# helium
# oxygen
