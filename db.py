import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from typing import Union
from google.cloud.firestore_v1.base_query import FieldFilter

# Use a service account.
cred = credentials.Certificate('c:/Users/musay/Desktop/smartphone-shop-1-firebase-adminsdk-52yyi-cc80f8bba9.json')

app = firebase_admin.initialize_app(cred, name='app1')

db = firestore.client(app=app)

cred2 = credentials.Certificate('c:/Users/musay/Desktop/card-smartshop-firebase-adminsdk-keojt-24c578d36c.json')

app2 = firebase_admin.initialize_app(cred2, name='app2')

db2 = firestore.client(app=app2)

def get_brends():
    brends = [i.id for i in db.collections()]
    return (brends)


def get_phones_by_brend(brend: str) -> list:
    if brend in get_brends():
        collection = db.collection(brend).stream()
        return [i.to_dict() for i in collection]

    return []
print(get_phones_by_brend('Apple'))

def get_phone_by_id(brend: str, doc_id: Union[str, int]):
    if brend in get_brends():
        return db.collection(brend).document(doc_id).get().to_dict()

def add_item(user_id: Union[int, str], brend: str, phone_id: Union[int, str]):
    data=({
        "user_id": user_id,
        "phone_id": phone_id,
        "brend": brend
    })
    db2.collection('item').add(data)
def get_items(user_id: Union[int, str]):

    items_collection = db2.collection('item')

    # User_id bo'yicha so'rov tuzish
    query = items_collection.where('user_id', '==', user_id)

    # So'rovni bajaring
    results = query.get()

    # Natijalarni olish
    items = [doc.to_dict() for doc in results]

    return items

def clear_items(user_id: Union[int, str]):
    items_collection = db2.collection('item')

    # User_id bo'yicha o'chirish uchun ma'lumotlarni topish
    query = items_collection.where('user_id', '==', user_id)
    results = query.get()

    # Topilgan ma'lumotlarni o'chirish
    for doc in results:
        doc.reference.delete()
    
print(clear_items('Jahongir'))