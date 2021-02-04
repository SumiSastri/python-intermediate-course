# IN THIS FILE:- unordered lists - dictionaries

symbol_to_name = {
    "H":  "hydrogen",
    "He": "helium",
    "Li": "lithium",
    "C":   "carbon",
    "o":   "oxygen",
    "N":   "nitrogen"
}

print(symbol_to_name)               # prints a list
print(len(symbol_to_name))          # prints number of key-value pairs
print(symbol_to_name.keys())        # prints a list of keys
print(symbol_to_name.values())      # prints a list of values
print(symbol_to_name.items())       # prints a tuple of key-value pairs
print()

symbol_to_name["N"] = "NITROGEN"
print(symbol_to_name)   # selects key with square brackets and mutates value
print()

# UPDATE METHOD
symbol_to_name.update({"K": "Potassium", "Ni": "Nickel", "Elements": ['e1', 'e2', [5, 6], True], "Planets": ('Mars','Venus')})
print(symbol_to_name)
print()

# GLOBAL DELETE METHOD
del symbol_to_name["Planets"]
print(symbol_to_name)


# CONTROL-FLOW TO CHECK KEYS AND VALUES
print()
print('*' * 20)
print()
if "He" in symbol_to_name:          # check for key
    print(symbol_to_name["He"])     # retrieve value

print()
print('*' * 20)
print()

for key, value in symbol_to_name.items():
    print("Key is %s and value is %s" % (key, value))    # prints the key and value of the whole dictionary
    print(symbol_to_name[key])                           #  returns the value of the key