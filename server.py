from flask import Flask, request, abort
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

@app.get("/api/categories")
def get_categories():
    categories = []
    cursor =db.products.find({})
    for prod in cursor:
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)

    return json.dumps(categories)

#get the list of products that belongs to given category
"""
create a results list
get the cursor with all products
travel the cursor
if the product category is equal to name
    fix the id and add product to results

return results

# get /api/products/category/A
# get /api/products/category/B
# get /api/products/category/C
# get /api/products/category/D

"""


@app.get("/api/products/category/<name>")
def get_by_category(name):
    results = []
    cursor = db.products.find({"category": name})
    for prod in cursor:
        results.append(fix_id(prod))

    return json.dumps(results)

# get /api/products/search/test
@app.get("/api/products/search/<term>")
def search_products(term):
    results = []
    cursor = db.products.find({"title":{"$regex": term, "$options":"i"} })
    for prod in cursor:
        results.append(fix_id(prod))

    return json.dumps(results)

#get api/products/lower/value
# to retrieve all products whose price is lower than a given value

@app.get("/api/products/lower/<value>")
def price_lower(value):
    results = []
    cursor = db.products.find({"price":{"$lt": float(value)} })
    for prod in cursor:
        results.append(fix_id(prod))

    return json.dumps(results)

#get api/products/lower/value
@app.get("/api/products/greater/<value>")
def price_greater(value):
    results = []
    cursor = db.products.find({"price":{"$gte": float(value)} })
    for prod in cursor:
        results.append(fix_id(prod))

    return json.dumps(results)

##################################
#########  coupon codes ##########
##################################

# GET /api/coupons          --> retrieve all
# POST /api/coupons         --> save new
# GET  /api/coupons/<code>  --> retrieve 1 by code


@app.post("/api/coupons")
def save_coupon():
    data = request.get_json()
    db.coupons.insert_one(data)

    print(data)
    return json.dumps(fix_id(data)) 

@app.get("/api/coupons")
def get_coupons():
    coupons = []
    cursor = db.coupons.find({})
    for coup in cursor:
        coupons.append(fix_id(coup))

    return json.dumps(coupons)

@app.get("/api/coupons/<code>")
def coupon_by_code(code):
    coupon = db.coupons.find_one({"code": code})
    if not coupon:
        return abort (404, "Invalid Code")
    
    return json.dumps(fix_id(coupon))





#app.run(debug=True)