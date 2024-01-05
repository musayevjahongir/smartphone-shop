from tinydb import TinyDB, Query
from typing import Union


db = TinyDB('db.json', indent=4)
cart = TinyDB('cart.json', indent=4)
item = cart.table('item')
q = Query()





def get_brends():
    brends = db.tables()
    return brends
# print(get_brends())

def get_phones_by_brend(brend: str) -> list:
    if brend in get_brends():
        collection = db.table(brend)
        return collection.all()

    return []

def get_phone_by_id(brend: str, doc_id: Union[str, int]):
    if brend in get_brends():
        collection = db.table(brend)
        phone = collection.get(doc_id=doc_id)
        return phone
# print(get_phone_by_id('Redmi', '2'))

def add_item(user_id: Union[int, str], brend: str, phone_id: Union[int, str]):
    item.insert({
        "user_id": user_id,
        "phone_id": phone_id,
        "brend": brend
    })

def get_items(user_id: Union[int, str]):
    items = item.search(q.user_id == user_id)
    return items
def clear_items(user_id: Union[int, str]):
    items = item.remove(q.user_id == user_id)
    return items
