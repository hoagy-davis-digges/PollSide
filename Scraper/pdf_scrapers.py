import xlrd, re
from Poll.models import *
pollster = Pollster.get(name='YouGov')

def yougov(file_address, poll_page_link):
    poll = Poll(url=poll_page_link)
    book = xlrd.open_workbook(filename=file_address)
    for sheet in book.get_sheets():
        last_data = True if re.match('\d{2}-\d{2}', ' '.join(cell.value for cell in sheet.col(2))) else False
        for cell in sheet.col(1):
            if cell.value.contains('Fieldwork'):
                category_row = sheet.row(sheet.col(1).index(cell)+1)
                break
        available_categories = Category.objects.values()
        used_categories = []
            for cell in category_row:
                if str(cell.value):
                    if Question.get()







