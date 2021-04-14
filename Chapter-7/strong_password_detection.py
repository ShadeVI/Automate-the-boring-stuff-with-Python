import re

passLengthRegex = re.compile(r'(.){8,}')
passLowerRegex = re.compile(r'[a-z]')
passUpperRegex = re.compile(r'[A-Z]')
passNumRegex = re.compile(r'\d')

# [valid, valid, not valid, not valid, not valid, not valid]
passwords = ["CscFNbqZRwsg3Ksu", "p3HpJfAZ", "pmYr28K",
             "bHKMPvzter", "gt29bma55wwes", "YR52EHS3SU4NC"]

for password in passwords:
    mo_length = passLengthRegex.search(password)
    if mo_length:
        length_checked = mo_length.group()
        mo_lower = passLowerRegex.search(length_checked)
        mo_upper = passUpperRegex.search(length_checked)
        mo_num = passNumRegex.search(length_checked)
        if mo_lower and mo_upper and mo_num:
            print("OK: " + length_checked)
