import csv
import json
import datetime
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
import time

start_time = time.time()
def get_context(autor_book, name_book, release_age, price_book):
    return {
        'autor': autor_book,
        'name': name_book,
        'release': release_age,
        'price': price_book
    }

def from_template(autor_book, name_book, release_age, price_book, template, signature):
    template = DocxTemplate(template)
    data = get_context(autor_book, name_book, release_age, price_book)

    img_size = Cm(7)
    acc = InlineImage(template, signature, img_size)
    data['acc'] = acc

    template.render(data)
    template.save(autor_book + '' + str(datetime.datetime.now().date()) + '_report.docx')

def generate_report(autor_book, name_book, release_age, price_book):
    template = 'book.docx'
    signature = 'acc.jpg'
    document = from_template(autor_book, name_book, release_age, price_book, template, signature)

def toFixed(numObj, digits = 0):
    return f'{numObj:.{digits}f}'

generate_report('Stephen King', 'Institute', 2020, 752)

finish_time = time.time()
gener_time = finish_time - start_time
print('Время создания отчета в формате .doc:', toFixed(gener_time, 4), 'секунды')

#csv

start_time_2 = time.time()

book_top = [['autor', 'name', 'release_age', 'price'], ['Stephen King', 'Institute', 2020, 752]]
with open('book_month.csv', 'w') as f:
    writer = csv.writer(f, delimiter = '|')
    writer.writerows(book_top)

finish_time_2 = time.time()
gener_time_2 = finish_time_2 - start_time_2
print('Время создания отчета в формате .csv:', toFixed(gener_time_2, 5), 'секунды')

#json

start_time_3 = time.time()

dict_book = {'autor': 'Stephen King', 'name': 'Institute', 'release_age': 2020, 'price': 752}
with open('dict_book_json.txt', 'w') as f:
    json.dump(dict_book, f)

finish_time_3 = time.time()
gener_time_3 = finish_time_3 - start_time_3
print('Время создания отчета в формате .json:', toFixed(gener_time_3, 5), 'секунды')