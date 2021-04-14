import re


def stripMethod(text, charToStrip="\s"):
    if charToStrip == "\s":
        text = re.sub(f'^{charToStrip}+', "", text)
        text = re.sub(f'{charToStrip}+$', "", text)
    else:
        text = re.sub(f'{charToStrip}', "", text)
    return text


stringToStrip = "      asd  as asd       asdasdas   a sd      "

print(stripMethod(stringToStrip, "asd"))
