from flask import Flask, request, abort
import json
from about import me
from config import db
from flask_cors import CORS

app = Flask(__name__) # create a instance of Flask class
CORS(app) # WARNING: disable CORS check


@app.get("/")
def home():
    return "Hello World from a flask server"


@app.get("/test")
def test():
    return "This is a test page"




@app.get("/api/version")
def version():
    return json.dumps("1.0")


@app.get("/api/about")
def about():
    return json.dumps(me)



@app.get("/api/developer/name")
def dev_name():
    name = me["name"]
    last = me["last_name"]
    email = me["email"]
    response = f"{name} {last} -- {email}"
    return json.dumps(response)




@app.get("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        results.append(fix_id(prod))

    return json.dumps(results)


def fix_id(record):
    record["_id"] = str(record["_id"])
    return record


@app.post('/api/catalog')
def save_product():
    product = request.get_json() # get the json payload from the request
    #save product to DB
    db.products.insert_one(product)

    return json.dumps(fix_id(product))





# get /api/products/count
# return the number of products in the catalog
@app.get("/api/products/count")
def product_count():
    count = db.products.count_documents({})
    return json.dumps(count)



@app.get("/api/products/total")
def sum_prices():
    cursor = db.products.find({})
    total = 0
    for product in cursor:
        price = product["price"]
        total = total + price


    print(total) # show the result in the terminal
    return json.dumps(total)


# get /api/categories
# return a list of categories
# 1 - create a list
# 2 - for to travel the catalog
    # 3 - get the category from the product
    # 4 add the category to the list
# 5 - return the list as json

@app.get("/api/categories")
def categories():
    # cursor
    cursor = db.products.find({})
    cats = []
    for prod in cursor:
        category = prod ["category"]

        # if category does not exist inside the list
        if category not in cats: 
            cats.append(category)

    return json.dumps(cats)


@app.get("/api/catalog/<category>")
def products_by_category(category):
   cursor = db.products.find({"category": category})
   results = []
   for prod in cursor:
       results.append(fix_id(prod))

   return json.dumps(results)



# should return all products whose price is lower than price var
@app.get("/api/products/lower/<price>")
def products_lower_price(price):
    fixed_price = float(price)
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        if prod["price"] < fixed_price:
            results.append(fix_id(prod))

    return json.dumps(results)


@app.get("/api/products/greater/<price>")
def products_greater_price(price):
    fixed_price = float(price)
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        if prod["price"] >= fixed_price:
            results.append(fix_id(prod))

    return json.dumps(results)



@app.get("/api/products/search/<term>")
def search_products(term):
    cursor = db.products.find({"title": { '$regex': term, "$options": "i" }})
    results = []
    for prod in cursor:
        results.append(fix_id(prod))

    return json.dumps(results)
   









####################################
########### COUPON CODES ###########
####################################

# GET /api/coupons  -> return all the coupons
# POST /api/coupons -> Save coupons
# { "code": "qwerty", "discount": 10 }

@app.post("/api/coupons")
def save_coupon():
    coupon = request.get_json()
    db.coupons.insert_one(coupon)

    return json.dumps(fix_id(coupon))

@app.get("/api/coupons")
def get_coupons():
    cursor = db.coupons.find({})
    results = []
    for coupon in cursor:
        results.append(fix_id(coupon))

    return json.dumps(results)



@app.get("/api/coupons/<code>")
def get_coupon_by_code(code):
    coupon = db.coupons.find_one({"code": code})
    if coupon == None:
        return abort(404, "Invalid coupon code")

    return json.dumps(fix_id(coupon))


# start the server
app.run(debug=True)