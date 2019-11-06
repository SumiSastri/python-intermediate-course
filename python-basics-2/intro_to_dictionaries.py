
symbol_to_name ={
    "H":  "hydrogen",
    "He": "helium",
    "Li": "lithium",
    "C":   "carbon",
    "o":   "oxygen",
    "N":   "nitrogen"
}
print(symbol_to_name)
print(len(symbol_to_name)) # prints a list
print(symbol_to_name.keys()) # prints a list
print(symbol_to_name.values()) # prints a list
print(symbol_to_name.items()) # prints a tuple
if "He" in symbol_to_name: # check for key
    print(symbol_to_name["He"]) # retrieve value

symbol_to_name["N"] = "NITROGEN"
print(symbol_to_name) # mutates value

symbol_to_name.update({"K": "Pottassium", "Ni": "Nickel", "Elements":['e1', 'e2', [5,6], True], "Planets": ('Mars', 'Venus')})
print(symbol_to_name)

print()
del symbol_to_name["Planets"]
print(symbol_to_name)

print()
for key, value in symbol_to_name.items():
    print("Key is %s and value is %s" %(key,value)) # prints the key and value
    print()
    print(symbol_to_name[key]) # returns the value of the key