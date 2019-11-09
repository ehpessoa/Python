#! python3
# text_files_to_spreadsheet.py
# usage: python text_files_to_spreadsheet.py {output_filename.xlsx} {txtfile} {txtfile2} {textfile3} ...

import sys
import openpyxl

# get name of output spreadsheet and the names of all the text files
if len(sys.argv) > 2:
    # load output worksheet
    output_filename = sys.argv[1]
    wb = openpyxl.Workbook()
    sheet = wb.active
    column_count = 1

    # load text files and iterate through
    for file in sys.argv[2:]:
        opened_file = open(file, 'r')
        opened_file_lines = opened_file.readlines()
        row_count = 1
        for line in opened_file_lines:
            sheet.cell(row=row_count, column=column_count).value = line
            row_count += 1
        # new column for next text file
        column_count += 1

    wb.save(output_filename)
else:
    print('python text_files_to_spreadsheet.py {output_filename.xlsx} {txtfile} {txtfile2} {textfile3} ...')
