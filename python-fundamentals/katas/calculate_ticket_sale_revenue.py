# Exercise 10 - Caluclate the revenue from ticket sales in a Doctor Who Film Festival.

print("SECTION 1 ***** " * 2)
print("Doctor who Festival\n")
print("SALES DESK:")
print("Category Price BreakDown")
adult_tickets = int(input("Enter  0 if none \n Adults: "))
under_16 = int(input("Enter  0 if none \n Under 16s: "))
family_of_four = int(input(" Enter 0 for none or \n 1 for a family of 4: "))
five_or_more = int(input("Enter 0 for none or \n Number in group:"))

individual_cost = adult_tickets * 68
under16_cost = under_16 * 32.25
family_discount = family_of_four * 42.75
group_discount = five_or_more * 59.99
print()

print("SECTION 2 ***** " * 2)
print("Category Price BreakDown")
print()
# %d is the place holder for result of the calculation %f is the placeholder for the variable
print("Price is %.2f for %d individuals" % (individual_cost, adult_tickets))
print("Price is %.2f for %d under 16s" % (under16_cost, under_16))
print("Price is %.2f for %d families" % (family_discount, family_of_four))
print("Price is %.2f for %d groups over 5" % (group_discount, five_or_more))
print()

print("SECTION 3 ***** " * 2)
print("Summary of sales")
print()
print("Total persons are %d" % (adult_tickets + under_16 + (family_of_four * 4) + five_or_more))
print("Total Event price is £%.2f" % (individual_cost + under16_cost + family_discount + group_discount))
print("For more info and booking visit our website")