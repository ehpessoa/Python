#! python3
# comma_code.py - Takes list and converts to sentence-ish with commas and an 'and'.

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(list):
    """
    Takes list and converts it to a string with commas, spacing, and an 'and'
    :param list: List of strings
    :return: String
    """
    new_list = list[:]
    new_list[-1] = 'and ' + list[-1]
    return ', '.join(new_list)

print(comma_code(spam))