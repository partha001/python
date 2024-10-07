import uuid

from flask import Flask
from flask_smorest import Api

from resources.item import blp as item_blueprint
from resources.store import blp as store_blueprint


app = Flask(__name__)

#some configuration
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores rest api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"]= "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(item_blueprint)
api.register_blueprint(store_blueprint)

#
# # api to get all store details
# @app.get("/store")
# def get_stores():
#     return {"stores": list(stores.values())}
#
#
# # api to create store
# # note: reading data post request payload
# # this api creates an empty store with zero items
# # request uri: http://localhost:5000/store
# # request payload:  {"name": "MyStore1"}
# @app.post("/store")
# def create_stores():
#     request_data = request.get_json()  #reads the post-request payload to a dictionary
#     storeId = uuid.uuid4().hex
#
#     for store in stores:
#         if (stores[store])["name"] == request_data["name"]:
#             return "store = {} already exists".format(request_data["name"]), 200
#
#     new_store = {"storeId": storeId, "name": request_data["name"], "items": []}
#     stores[storeId] = new_store
#     return new_store, 201
#
#
# # api to get details of a particular store
# #  http://localhost:5000/store/getStoreDetails?storeId=ae4445f6545546e3b51a0cacd0b4c525
# @app.get("/store/getStoreDetails")
# def get_store_details():
#     storeId = request.args.get('storeId')
#     if storeId not in stores:
#         return stores.get(storeId), 200
#     #return "store with storeId = {} not found".format(storeId), 404
#     abort(404, message="store with storeId = {} not found".format(storeId))
#
#
# # api to create items within a particular store
# # http://localhost:5000/item
# # {"name": "Table","price":20, "storeId":"100"}
# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#     if (
#         "price" not in item_data
#         or "storeId" not in item_data
#         or "name" not in item_data
#     ):
#         abort(
#             400,
#             message="Bad request. ensure price, storeId and name is present included in json payload"
#         )
#     if item_data["storeId"] not in stores:
#         #return "storeId:{} is not found ".format(item_data["storeId"]), 404
#         abort(404, message="storeId:{} is not found ".format(item_data["storeId"]))
#
#     itemId = uuid.uuid4().hex
#     item = {**item_data, "itemId": itemId}
#     items[itemId] = item
#     return item, 201
#
#
# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}, 200
#
#
# @app.get("/items/<string:itemId>")
# def get_item_with_itemid(itemId):
#     if itemId not in items:
#         return "item with itemId:{} not found".format(itemId)
#     return items[itemId], 200
