

# captures user input
phrase = input()

# outputs the results, counts number of times the first letter in the phrase is present minus the initial character
print(phrase.count(phrase[0]) - 1)
