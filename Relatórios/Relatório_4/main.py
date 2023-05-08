from database import Database
from writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
db.resetDatabase()


result2 = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {
        "_id": {"$dateToString": {"format": "%Y-%m-%d", "data": "$data"}},
        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
    }},
    {"$sort": {"_id": 1}}
])

writeAJson(result2, "Total de vendas por dia")

# # Cliente que mais comprou em cada dia:
# result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#     {"$sort": {"_id.data": 1, "total": -1}},
#     {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
# ])

# writeAJson(result, "Cliente que mais comprou em cada dia")

# # Produto mais vendido: