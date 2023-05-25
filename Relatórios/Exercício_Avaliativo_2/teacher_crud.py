class TeacherCRUD:
    def __init__(self, db):
        self.db = db

    def create(self, name, ano_nasc, cpf):
        query = f"CREATE(:Teacher{{name:'{name}', ano_nasc:{ano_nasc}, cpf:'{cpf}'}})"
        self.db.execute_query(query)

    def read(self, name):
        query = f"MATCH(t:Teacher{{name:'{name}'}}) RETURN t"
        result = self.db.execute_query(query)
        return [record['t'] for record in result]

    def delete(self, name):
        query = f"MATCH(t:Teacher{{name:'{name}'}}) DETACH DELETE t"
        self.db.execute_query(query)

    def update(self, name, new_cpf):
        query = f"MATCH(t:Teacher{{name:'{name}'}}) SET t.cpf = '{new_cpf}'"
        self.db.execute_query(query)

    def close(self):
        self.db.close()