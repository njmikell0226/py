lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#friends.extend() - to add list on the end of the exsisting friends list
#friends.append() - add another item to the end of the list
#friends.insert(1, "Kelly") - 2 paramerters, the index where you want to insert , element
#friends.remove("Jim")
#friends.clear - remove all elements
#friends.pop() - pop an item off of the list (last itemm removed)

# print(friends.index("Kevin")) - to find index of item
# print(friends.count("Jim")) - to count number of values

#lucky_numbers.sort() - sorts in alphabetically order
#lucky_numbers_reverse() - reverse order

#friends2 = friends.copy() - take a copy of a list

lucky_numbers.reverse()
print(lucky_numbers)