
#get money variable amount from user input interger
money = int(input())

#if money is equal to or less than 0 output No change
if money <= 0:
    print('No change')

# money variable divided by its value in cents, in order from largest to smallest
#quarters calculation and output if equal to 1, else if variable is greater then 1 make string plural
dollars = money // 100
if dollars > 0 and money > 0:
    money = money - (dollars * 100)
if dollars == 1:
    print(dollars, 'Dollar')
elif dollars > 1:
    print(dollars, 'Dollars')

#quarters calculation and output if equal to 1, else if variable is greater then 1 make string plural
quarters = money // 25
if quarters > 0 and money > 0:
    money = money - (quarters * 25)
if quarters == 1:
    print(quarters, 'Quarter')
elif quarters > 1:
    print(quarters, 'Quarters')

#dimes calculation and output if equal to 1, else if variable is greater then 1 make string plural
dimes = money // 10
if dimes > 0 and money > 0:
    money = money - (dimes * 10)
if dimes == 1:
    print(dimes, 'Dime')
elif dimes > 1:
    print(dimes, 'Dimes')

#nickels calculation and output if equal to 1, else if variable is greater then 1 make string plural
nickles = money // 5
if nickles > 0 and money > 0:
    money = money - (nickles * 5)
if nickles == 1:
    print(nickles, 'Nickel')
elif nickles > 1:
    print(nickles, 'Nickles')

#pennies calculation and output if equal to 1, else if variable is greater then 1 make string plural
pennies = money // 1
if pennies > 0 and money > 0:
    money = money - (pennies * 1)
if pennies == 1:
    print(pennies, 'Penny')
elif pennies > 1:
    print(pennies, 'Pennies')