# print method - uncomment to check

# word_to_check = 'mom'
word_to_check = "god"
# word_to_check = 'saas'
# word_to_check = 'madam'
# word_to_check = 'madman'
# word_to_check = 'deed'

if word_to_check != word_to_check[::-1]:
    print("Sorry, %s isn't a palindrome"% (word_to_check))
else:
    print("Yep! %s is a palindrome" % (word_to_check))

# input method
word = input("Enter a word  ")
print('%s' % word)
word = (str(word))
if word != word[::-1]:
    print("Sorry, %s isn't a palindrome"% (word))
else:
    print("Yep! %s is a palindrome" % (word))



