# FIXME (1): Finish reading another word and an integer into variables.

favorite_color = input('Enter favorite color:\n')
favorite_girlname = input('Enter favorite girl name:\n')
favorite_number = input('Enter favorite number:\n')

# assigned password combinations to variables to use count method
password1 = favorite_color +'_'+ favorite_girlname
password2 = favorite_number + favorite_color + favorite_number

# output all the values on a single line
print('You entered:', favorite_color, favorite_girlname, favorite_number)

# FIXME (2): Output two password options
print('\nFirst password:', password1)
print('Second password:', password2)


# FIXME (3): Output the length of the two password options
print('\nNumber of characters in', password1 + ":", password1.count('') -1)
print('Number of characters in', password2 + ":", password2.count('') -1)
