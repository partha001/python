from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name" : "MyStore",
        "items" :[
            {
                "name":"Chair",
                "price": 15.99
            }
        ]
    }
]


@app.get("/store")
def get_stores():
    return {"stores":stores}

### reading data post request payload
### this api creates an empty store with zero items
# request uri: http://localhost:5000/store
# request payload:  {"name": "MyStore1"}
@app.post("/store")
def create_stores():
    request_data = request.get_json() #reads the post-request payload to a dictionary

    store_exists = False
    for store in stores:
        if store["name"] == request_data["name"]:
            new_store = {"name": request_data["name"],"items":[]}
            stores.append(new_store)
            return "store = {} created".format(request_data["name"]), 201
    return "store = {} already exists".format(request_data["name"]), 200



### taking the store name as path-param
## http://localhost:5000/store/MyStore1/item
# {"name": "Table","price":20}
@app.post("/store/<string:name>/item")
def create_item(name):
    print("requested store name is : {}".format(name))
    request_data = request.get_json() #reads the post-request payload to a dictionary
    for store in stores:
        if store["name"] == name:
            new_item  = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item,201
    return "store={} not found".format(name), 200

