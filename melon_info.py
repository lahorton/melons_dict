"""Print out all the melons in our inventory."""


from melons import melons


# def print_melon(name, seedless, price):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f"{name}s {have_or_have_not} seeds and are ${price:.2f}")


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])


def print_melon_attribute(melons):
    """prints out the attributes of each type of melon"""

     # melon_name = {name: {inner_dictionary of attributes}}
     # attributes = {seedless:T/F, price:_, flesh_color: _, weight: _, rind_color:_}

    for melon, attribute in melons.items():
        print(melon)
        for attribute, value in melons.values():
            print('{} : {}'.format(attribute, value)

print_melon_attribute(melons)
