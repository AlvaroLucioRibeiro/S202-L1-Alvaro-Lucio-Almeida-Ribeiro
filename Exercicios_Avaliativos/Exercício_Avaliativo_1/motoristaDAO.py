from bson.objectid import ObjectId
from motorista import *


class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create(self, motorista: Motorista):
        try:
            res = self.db.collection.insert_one(vars(motorista))
            print(f"Motorista criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None

    def read(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista found")
            return res
        except Exception as e:
            print(f"An error occurred while reading motorista: {e}")
            return None

    def update(self, id: str):
        try:
            motorista = self.db.collection.find_one({"id": ObjectId(id)})
            nota = [i["nota"] for i in motorista["corridas"]]
            notafinal = sum(nota) / len(nota)
            motorista["nota"] = notafinal

            res = self.db.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": motorista}
            )
            print(f"Motorista  updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating motorista: {e}")
            return None

    def delete(self, id: str):
        try:
            res = self.db.collection.delete_one({"id": ObjectId(id)})
            print(f"motorista deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None
