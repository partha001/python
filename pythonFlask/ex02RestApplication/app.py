import uuid

from flask import Flask, request
from db import items, stores

app = Flask(__name__)


# api to get all store details
@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


# api to create store
# note: reading data post request payload
# this api creates an empty store with zero items
# request uri: http://localhost:5000/store
# request payload:  {"name": "MyStore1"}
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
#  http://localhost:5000/store/getStoreDetails?storeId=ae4445f6545546e3b51a0cacd0b4c525
@app.get("/store/getStoreDetails")
def getStoreDetails():
    storeId = request.args.get('storeId')
    if storeId in stores:
        return stores.get(storeId), 200
    return "store with storeId = {} not found".format(storeId), 200


# api to create items within a particular store
# http://localhost:5000/item
# {"name": "Table","price":20, "storeId":"100"}
@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["storeId"] not in stores:
        return "storeId:{} is not found ".format(item_data["storeId"]), 404

    itemId = uuid.uuid4().hex
    item = {**item_data, "itemId": itemId}
    items[itemId] = item
    return item, 201


@app.get("/items")
def get_all_items():
    return {"items": list(items.values())}, 200


@app.get("/items/<string:itemId>")
def get_item_with_itemid(itemId):
    if itemId not in items:
        return "item with itemId:{} not found".format(itemId)
    return items[itemId], 200
