#true and false are called booleans

#usually things are hard coded to true or false. You want to build a block of code that evaluates to true or false. 



#Comparision:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     > 
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

language = 'Python'

if language == 'Python':
    print('Conditional was True')
else:
    print('No Match')

#no match - executed else code block
language2 = 'Java'

if language2 == 'Python':
    print('Conditional was True')
else:
    print('No Match')

#evaulate multiple conditions with the elif statement

language3 = 'Java'

if language3 == 'Python':
    print('Conditional was True')
elif language3 == 'Java':
    print('Language is Java')
else:
    print('No Match')

#boolean operators
# and
# or
# not

user = 'Admin'

logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

