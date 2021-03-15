table_data = [
    ['apples','oranges','cherries','banana'],
    ['Alice','Bob','Carol','David'],
    ['dogs','cats','moose','goose']
]

def get_longest_strings(data):
    longest_strings = [0] * len(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if len(data[i][j]) > longest_strings[i]:
                longest_strings[i] = len(data[i][j])
    return longest_strings

def print_table(data):
    col_widths = get_longest_strings(data)
    for i in range(len(data[0])): # 0 - 3
        for j in range(len(data)): # 0 - 2
            print(data[j][i].rjust(col_widths[j]), end=" ") # print data[0][0] data[1][0] data[2][0] in a row
        print()

print_table(table_data)