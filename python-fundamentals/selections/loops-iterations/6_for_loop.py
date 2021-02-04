# IN THIS FILE:- FOR-LOOP
#  Syntax for x in y where for and in are key-words followed by colon
#  Can be used on all data-types

# FOR-LOOP
symbol_to_name = {
        "H": "hydrogen",
        "He": "helium",
        "Li": "lithium",
        "C": "carbon",
        "o": "oxygen",
        "N": "nitrogen"
    }

for key, value in symbol_to_name.items():
        print("Key is %s and value is %s" % (key, value))  # prints the key and value
        print()
        print(symbol_to_name[key])  # returns the value of the key
