import re

# from lipsom.com

s1 = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ut nibh metus. Mauris id fermentum orci. Duis feugiat malesuada lorem, sed tristique ligula rutrum luctus. Quisque tincidunt tortor at cursus dictum. Vivamus euismod hendrerit diam, at porta velit. Nulla pharetra, orci porta lacinia volutpat, arcu risus feugiat odio, in rhoncus erat tellus a elit. Quisque eget malesuada lacus, vitae euismod purus. Etiam porttitor, quam a gravida imperdiet, lacus est molestie nulla, nec hendrerit nisi ipsum quis lectus. Fusce rhoncus vehicula turpis non venenatis. Praesent non lobortis tortor. '''

print(r'\n') # raw string - raw stands for the pattern of the text

list1 = re.findall(r's\w+', s1) # patterns and source string, identifiers and modifiers
print(list1)
list2 = re.findall(r'\bs\w+', s1) # \b identifier beginning of word \w word \d digit \s whitespace \.period
print(list2) # modifiers + one or more occurrence  *zero or more occurence ? zero or one occurence m,n number of repititions a-e between ^ at the beginning of $ at the end of  | or

list2 = re.findall(r'\b\d(1,4)\w', s1)
print(list2)

list3 = re.findall(r'\b[a-e|p-s]\w+', s1, re.I) # by default it is case sensitive I means case insensitive
print(list3)

list4 = re.findall(r'^simply', s1)
print(list4)

list5 = re.findall(r'^L\w+', s1)
print(list5)

list6 = re.findall(r'ipsum.$', s1)
print(list6)

print(re.sub(r'dolor', 'DOLOR', s1, 0, re.I)) # replaces 1 instances if count 0 replaces all flags re.I

# list6 = re.search(r'sed', s1)
list6 = re.match(r'sed', s1)# looks for the first word only
if list6:
    print(list6.group()) # first match
    print(list6.span()) # first occurance
else:
    print('doesn\'t exist')
