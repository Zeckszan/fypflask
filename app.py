import pyrebase
from flask import Flask, jsonify
import re

app = Flask(__name__)

english_to_malay = {
    'apple': 'epal',
    'banana': 'pisang',
    'beetroot': 'bit',
    'bell pepper': 'lada besar',
    'cabbage': 'kubis',
    'capsicum': 'kapsikum',
    'carrot': 'lobak',
    'cauliflower': 'kubis bunga',
    'chilli pepper': 'lada cili',
    'corn': 'jagung',
    'cucumber': 'timun',
    'eggplant': 'terung',
    'garlic': 'bawang putih',
    'ginger': 'halia',
    'grapes': 'anggur',
    'jalepeno': 'jalepeno',
    'kiwi': 'kiwi',
    'lemon': 'limau',
    'lettuce': 'selada',
    'mango': 'mangga',
    'onion': 'bawang besar',
    'orange': 'oren',
    'paprika': 'paprika',
    'pear': 'pir',
    'peas': 'kacang pea',
    'pineapple': 'nanas',
    'pomegranate': 'delima',
    'potato': 'kentang',
    'raddish': 'lobak merah',
    'soy beans': 'kacang soya',
    'spinach': 'bayam',
    'sweetcorn': 'jagung manis',
    'sweetpotato': 'ubi keledek',
    'tomato': 'tomato',
    'turnip': 'kubis air',
    'watermelon': 'tembikai'
}

@app.route("/")
def home():
    return "successfully called"


@app.route("/get/<productname>")
def filter(productname):
    config = {
        "apiKey": "AIzaSyCvrfjVrBgcobvJgYcE_Yda7OrN3xbBhoQ",
        "authDomain": "pricescrape2.firebaseapp.com",
        "projectId": "pricescrape2",
        "databaseURL": "https://pricescrape2-default-rtdb.firebaseio.com/",
        "storageBucket": "pricescrape2.appspot.com",
        "messagingSenderId": "83119362702",
        "appId": "1:83119362702:web:b89a01e53e3dbd3f202fdf",
        "measurementId": "G-Z27T8MYY96"
    }
    firebase = pyrebase.initialize_app(config)
    database = firebase.database()

    dataJaya = database.child("jaya grocer").get()
    dataVillage = database.child("village grocer").get()
    dataLotus = database.child("lotus").get()

    dataJaya = dataJaya.val()
    dataVillage = dataVillage.val()
    dataLotus = dataLotus.val()

    print(dataJaya)
    print(dataVillage)
    print(dataLotus)

    listJaya =['Jaya Grocer']
    pattern = re.compile(r'\b{}\b'.format(re.escape(productname)), re.IGNORECASE)

    listJaya.extend([(product['product_name'], product['price']) for product in dataJaya
                     if re.search(pattern, product['product_name'])])

    listVillage =['Village Grocer']
    listVillage.extend([(product['product_name'], product['price']) for product in dataVillage
                        if re.search(pattern, product['product_name'])])

    productname = english_to_malay[productname]
    listLotus =['Lotus']
    listLotus.extend([(product['product_name'], product['price']) for product in dataLotus
                      if re.search(pattern, product['product_name'])])

    return listJaya+listVillage+listLotus



# read from firebase and give app the filtered result
if __name__ == '__main__':
    app.run()


