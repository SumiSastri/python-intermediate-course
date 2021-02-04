# IN THIS FILE:- Selections are referred to as statements - here we will look at the if statement

# CONTROL-FLOW INTRODUCTION
#  Selection or control-flow is how programs make boolean choices in executing code blocks
#  selections are code blocks not methods as a prescribed flow must be followed but variables are allowed
#  the flow starts with a variable assignment, a test statement is declared
#  the statement is checked if true a code block is run

# IF Statement
symbol_to_name = {
    "H": "hydrogen",
    "He": "helium",
    "Li": "lithium",
    "C": "carbon",
    "o": "oxygen",
    "N": "nitrogen"
}  # variable assignment

if "He" in symbol_to_name:  # test statement declared with colon check for the key
    print(symbol_to_name["He"])  # run suite
