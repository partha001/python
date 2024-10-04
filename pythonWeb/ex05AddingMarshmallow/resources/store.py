import uuid
#from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema

blp = Blueprint("stores", __name__, description="Operations on store")


@blp.route("/store")
class Store(MethodView):

    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values(), 200

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        #store_data = request.get_json()  #reads the post-request payload to a dictionary
        storeId = uuid.uuid4().hex

        for store in stores:
            if (stores[store])["name"] == store_data["name"]:
                return "store = {} already exists".format(store_data["name"]), 200

        new_store = {"storeId": storeId, "name": store_data["name"], "items": []}
        stores[storeId] = new_store
        return new_store, 201


@blp.route("/store/<string:storeId>")
class StoreIdApis(MethodView):

    @blp.response(200, StoreSchema)
    def get(self, storeId):
        try:
            return stores[storeId]
        except KeyError:
            abort(404, message="store with storeId = {} not found".format(storeId))

    def delete(self, storeId):
        try:
            del stores[storeId]
            return {"message": "store with deleted successfully "}, 200
        except KeyError:
            abort(404, message="store with storeId = {} not found".format(storeId))
