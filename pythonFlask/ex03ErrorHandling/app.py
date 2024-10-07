import uuid

from flask import Flask, request
from db import items, stores
from flask_smorest import abort

app = Flask(__name__)


# api to get all store details
@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


# sample payload: {    "name":"mystore"}
@app.post("/store")
def create_stores():
    request_data = request.get_json()  #reads the post-request payload to a dictionary
    storeId = uuid.uuid4().hex

    for store in stores:
        if (stores[store])["name"] == request_data["name"]:
            return "store = {} already exists".format(request_data["name"]), 200

    new_store = {"storeId": storeId, "name": request_data["name"], "items": []}
    stores[storeId] = new_store
    return new_store, 201


# api to get details of a particular store
#  http://localhost:5000/store/0e7a29d0a57e49bb902887a05a64fe31
@app.get("/store/<string:storeId>")
def get_store_details(storeId):
    try:
        return stores[storeId]
    except KeyError:
        abort(404, message="store with storeId = {} not found".format(storeId))

@app.delete("/store/<string:storeId>")
def delete_store_details(storeId):
    try:
        del stores[storeId]
        return {"message":"store with deleted successfully "},200
    except KeyError:
        abort(404, message="store with storeId = {} not found".format(storeId))

@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}, 200



# http://localhost:5000/item
# {"name": "Table","price":20, "storeId":"100"}
@app.post("/item")
def create_item():
    item_data = request.get_json()
    print(item_data)
    if (
        "price" not in item_data
        or "storeId" not in item_data
        or "name" not in item_data
    ):
        abort(
            400,
            message="Bad request. ensure price, storeId and name is present included in json payload"
        )
    if item_data["storeId"] not in stores:
        abort(404, message="storeId:{} is not found ".format(item_data["storeId"]))

    itemId = uuid.uuid4().hex
    item = {**item_data, "itemId": itemId}
    items[itemId] = item
    return item, 201


@app.get("/item/<string:itemId>")
def get_item_with_itemid(itemId):
    try:
        return items[itemId]
    except KeyError:
        abort(404, message="item with itemId = {} not found".format(itemId))

@app.delete("/item/<string:itemId>")
def delete_item_with_itemid(itemId):
    try:
        del items[itemId]
        return {"message":"item deleted successfully"},200
    except KeyError:
        abort(404, message="item with itemId = {} not found".format(itemId))

@app.put("/item/<string:itemId>")
def update_item_with_itemid(itemId):
    item_data = request.get_json()
    if "price" not in item_data or "name" not in item_data:
        abort(400, message= "Bad request. Ensure price and name are included in json payload")

    try:
        item = items[itemId]
        item |= item_data #this dictionary operator does in place replacement
        return item, 200
    except KeyError:
        abort(404, message="item with itemId = {} not found".format(itemId))

