import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('c:/Users/musay/Desktop/smartphone-shop-1-firebase-adminsdk-52yyi-cc80f8bba9.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()