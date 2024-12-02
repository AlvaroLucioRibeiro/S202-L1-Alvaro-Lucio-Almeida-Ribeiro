# Nome: Álvaro Lúcio Almeida Ribeiro
# Matrícula: 163
# Exercício Avaliativo 2

from database import Database

db = Database("bolt://18.206.250.26:7687", "neo4j", "twist-film-offers")
# --------------------------------------------------------------------------------------- #
# Questão 1
result = db.execute_query("MATCH(t:Teacher{name:'Renzo'}) RETURN t.ano_nasc, t.cpf")
print("Resultado da consulta 1:")
for record in result:
    print(record["t.ano_nasc"], record["t.cpf"])

result = db.execute_query(
    "MATCH(t:Teacher) WHERE t.name STARTS WITH $letter RETURN t.name, t.cpf",
    parameters={"letter": "M"},
)
print("\nResultado da consulta 2:")
for record in result:
    print(record["t.name"], record["t.cpf"])

result = db.execute_query("MATCH(c:City) RETURN c.name")
print("\nResultado da consulta 3:")
for record in result:
    print(record["c.name"])

result = db.execute_query(
    "MATCH(s:School) WHERE s.number >= $min_number AND s.number <= $max_number RETURN s.name, s.address, s.number",
    parameters={"min_number": 150, "max_number": 550},
)
print("\nResultado da consulta 4:")
for record in result:
    print(record["s.name"], record["s.address"], record["s.number"])

# --------------------------------------------------------------------------------------- #
# Questão 2
result = db.execute_query(
    "MATCH(t:Teacher) RETURN min(t.ano_nasc) as min_year, max(t.ano_nasc) as max_year"
)
print("\nResultado da consulta 5:")
for record in result:
    print(f"Ano mínimo: {record['min_year']}, Ano máximo: {record['max_year']}")

result = db.execute_query("MATCH(c:City) RETURN avg(c.population)")
print("\nResultado da consulta 6:")
for record in result:
    print(record[0])

result = db.execute_query(
    "MATCH(c:City{cep:'37540-000'}) RETURN replace(c.name, 'a', 'A')"
)
print("\nResultado da consulta 7:")
for record in result:
    print(record[0])

result = db.execute_query("MATCH(t:Teacher) RETURN substring(t.name, 2)")
print("\nResultado da consulta 8:")
for record in result:
    print(record[0])
