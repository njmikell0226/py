import datetime

# prompts the user to input name and age and assign to variables
name = input ('What is your name?: ')
age = input ('How old are you?: ')

# utilize the datetime module to import the date to avoid another user prompt, and deduct age from user input
current_year = datetime.datetime.now()
year_born = current_year.year - int(age)

# output text in the form of a single sentence
print('\nHello', name +'!', 'You were born in', str(year_born) +'.')