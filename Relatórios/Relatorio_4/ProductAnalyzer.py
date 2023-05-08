from database import Database
from writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
db.resetDatabase()

# Exercício 1
def total_vendas_por_dia():
    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
    ])
    writeAJson(result, "Total de vendas por dia")

# Exercício 2
def produto_mais_vendido():
    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$sortByCount": "$produtos.descricao"},
        {"$limit": 1}
    ])
    writeAJson(result, "Produto mais vendido em todas as compras")

# Exercício 3
def cliente_que_mais_gastou():
    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$cliente_id", "total_compra": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        {"$sort": {"total_compra": -1}},
        {"$limit": 1}
    ])
    writeAJson(result, "Cliente que mais gastou em uma única compra")

# Exercício 4
def produtos_com_quantidade_vendida_acima_de_1_unidade():
    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$match": {"produtos.quantidade": {"$gt": 1}}},
        {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}}
    ])
    writeAJson(result, "Produtos com quantidade vendida acima de 1 unidade")

total_vendas_por_dia()
produto_mais_vendido()
cliente_que_mais_gastou()
produtos_com_quantidade_vendida_acima_de_1_unidade()