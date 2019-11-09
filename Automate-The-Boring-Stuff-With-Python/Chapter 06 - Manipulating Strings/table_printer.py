#! python3
# table_printer.py - takes a list of list with same length, displays each inner_list vertically

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['alice', 'bob', 'carol', 'derrick'],
              ['dogs', 'cats', 'fish', 'frogs']]


def print_table(table):
    # find how many inner lists
    num_of_lists = len(table[0])

    # iter through each index in the inner lists
    for i in range(num_of_lists):
        # init the place holder
        row = ''
        # iter through each list in the table
        for inner_list in table:
            # get the max letters for inner list, is there a way to do this once and refer to it?
            letter_count = max(len(word) for word in inner_list)
            # add the word to the row, with justification right + 1 for an extra space
            row += (inner_list[i].rjust(letter_count + 1, ' '))
        print(row)


print_table(table_data)
