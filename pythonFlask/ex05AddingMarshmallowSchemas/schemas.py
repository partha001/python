from marshmallow import Schema, fields

class StoreSchema(Schema):
    storeId = fields.Str(dump_only=True) #since it will never be and input and will always be generated at backend
    name = fields.Str(required=True) #since it will come as part of input

class ItemSchema(Schema):
    itemId = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    storeId = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

