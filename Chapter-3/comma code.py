spam = ['apples', 'bananas', 'tofu', 'cats']


def createString(listSpam):
    newString = ''
    for index, item in enumerate(listSpam):
        if index == 0:
            newString += item
        elif index > 0 and index < len(listSpam) -1:
            newString += ', ' + item
        else:
            newString += ' and ' + item
    return newString

print(createString(spam))
