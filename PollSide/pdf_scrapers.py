import xlrd, re
from Poll.models import *

def yougov(file_address):
    book = xlrd.open_workbook(filename=file_address)
    for sheet in book.get_sheets():
        last_data = True if re.match('\d{2}-\d{2}', ' '.join(cell.value for cell in sheet.col(2))) else False
        for cell in sheet.col(1):
            if cell.value.contains('Fieldwork'):
                category_row = sheet.row(sheet.col(1).index(cell)+1)
                break
        for cell in category_row:
            if cell.value:
                cell.


