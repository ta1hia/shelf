import xmltodict
import os
import json
import requests

KEY = os.environ.get("GOODREADS_ACCESS_KEY")
PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

def request_user_shelves(parms):
    p = dict(parms)
    p.update({"key": KEY})
    resp = requests.get("https://www.goodreads.com/shelf/list.xml",p)
    data_dict = xmltodict.parse(resp.content)
    data_dict = data_dict['GoodreadsResponse']['shelves']
    shelf_count = {}
    for shelf in data_dict['user_shelf']:
        shelf_count[str(shelf['name'])] = int(shelf['book_count']['#text'])
    return shelf_count

def request_shelf_books(parms):
    p = dict(parms)
    p.update({"key":os.environ.get("GOODREADS_ACCESS_KEY"), "v":"2"})
    resp = requests.get("https://www.goodreads.com/review/list.xml/", p)
    data_dict = xmltodict.parse(resp.content)
    data_dict = data_dict['GoodreadsResponse']['reviews']['review']
    books = []
    for book in data_dict:
        books.append({"title": book['book']['title'].strip(" "), "author":book['book']['authors']['author']['name']})
    return books

def create_shelf_file():
    if KEY is None:
        print("GOODREADS_ACCESS_KEY not set")
        return
    shelf_info = request_user_shelves({"user_id": "4933497-tahia"})
    shelves = []
    for name,total in shelf_info.items():
        pg = 1
        left = total
        books = []
        while left > 0:
            books.extend(request_shelf_books({"shelf": name, "id": "4933497-tahia", "per_page":200, "page":pg}))
            left -= 200
            pg+=1
        shelves.append({"name":name, "total":total, "books":books})
    with open(os.path.join(PATH, 'shelf.tmp.json'), 'w') as outfile:
        json.dump(shelves, outfile)
    format_data()


def format_data():
    temp_file = os.path.join(PATH, 'shelf.tmp.json')
    f1 = open(temp_file, 'r+')
    content = f1.read()
    f1.seek(0,0)

    data_file = os.path.abspath(os.path.join(PATH, "js", "data.js"))
    try:
        os.remove(data_file)
    except OSError:
        pass
    f2 = open(data_file, 'w')
    f2.write("var data = '" + content.replace("'", "&#39;") + "';")
    f1.close()
    f2.close()


create_shelf_file()

