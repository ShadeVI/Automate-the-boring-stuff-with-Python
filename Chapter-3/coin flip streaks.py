import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values
    listOfFlips = []
    for i in range(100):
        if random.randint(0,1) == 0:
            listOfFlips.append('H')
        else:
            listOfFlips.append("T")
    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 0
    for index, item in enumerate(listOfFlips):
        if index > 0:
            if item == listOfFlips[index-1]:
                streak += 1
            else:
                streak = 0
        if streak == 6:
            numberOfStreaks += 1
    
print('Chance of streaks: %s%%' % (numberOfStreaks / 100))