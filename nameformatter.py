
# collects users name
user_name = 'Michael Little'#input()

# splits entered name into seperate list items
individual_names = user_name.split()

# x variable for word count, variable created for each part of the user_name, using negative to indicate last word = last name
x = len(individual_names)
first_name = individual_names[0]
middle_name = individual_names[1]
last_name = individual_names[-1]

# x variable is the number of words used in the user_name, determines format printed.
if x == 3:
   print(last_name +',', first_name[0]+'.'+ middle_name[0]+'.')
else:
   print(last_name +',', first_name[0]+'.')
