from flask import Flask, request
import json
from config import db

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask"

@app.get("/test")
def test():
    return "This is another page"




#### API ENDPOINTS ####
######   JSON      ###

def fix_id(obj):
    #fix the object to be json parsable
    obj["_id"] = str(obj["_id"])
    return obj

@app.get("/api/about")
def about():
    me = {"name": "Eloim Arreola"}
    return json.dumps(me)

@app.get("/api/catalog")
def get_catalog():
    products = []
    cursor = db.products.find({})
    for prod in cursor:
        products.append(fix_id(prod))

    return json.dumps(products)

@app.post("/api/catalog")
def save_product():
    data = request.get_json()
    db.products.insert_one(data)

    print(data) #to terminal
    return json.dumps(fix_id(data)) #will fail


#get /api/total
# return the total value of your catalog (the sum of all prices)

@app.get("/api/total")
def total_value():
    cursor = db.products.find({})
    total = 0
    for prod in cursor:
        total += prod["price"]
    
    return json.dumps(total)

@app.get("/api/products")
def count_products():
    cursor = db.products.find({})
    count = 0
    for prod in cursor:
        count+= 1

    return json.dumps(count)



app.run(debug=True)