"""
    this script...
    imports excel files and converts them into a python array
    imports sas files and coverts them into a python array
    exports python arrays to excel files
    exports python arrays to sas files
"""

import pandas as pd

file_name = input('what is the excel file name? ')
sheet_name = input('what is the workbook sheet name? ')

spread_sheet = pd.read_excel('C:/Users/cnt_47754/Desktop/' + file_name, sheet_name=sheet_name)

column_headers = spread_sheet.columns
column_values = spread_sheet.values


for column in column_headers:
    if column == 'full_term_wp':
        print(column_values[column.index][5])