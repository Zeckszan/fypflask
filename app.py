import pyrebase




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

# data = [
#     {'product_name': 'Dole Banana (Philippines) 1pack', 'price': 'RM 8.20'},
#     {'product_name': 'Ipoh Bean Sprout in Cup (Malaysia) 3456', 'price': 'RM 2.50'},
# ][]


#@app.route('/<productname>')
def filter():
    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    data = database.child("users").get()
    print(data.val())
    data = data.val()
    #data = jsonify(data.val())

    productname = 'epal'

    productsreturn = [(product['product_name'], product['price']) for product in data if
                      str(productname).lower() in product['product_name'].lower()]

    print("productsreturn ", productsreturn)
    return productsreturn


# read from firebase and give app the filtered result
if __name__ == '__main__':
    app.run()


