class Game:
    def __init__(self, db):
        self.db = db
        
    def create_player(self, player_id, player_name):
        query = "CREATE (:Player {id: $player_id, name: $player_name})"
        parameters = {"player_id": player_id, "player_name": player_name}
        self.db.execute_query(query, parameters)

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        result = self.db.execute_query(query, parameters)

    def delete_player(self, player_id):
        query = "MATCH (p:Player) WHERE id(p) = $player_id DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p"
        result = self.db.execute_query(query)
        return [record["p"] for record in result]

    def create_match(self, player_ids, result):
        query = "CREATE (m:Match {result: $result}) RETURN m"
        parameters = {"result": result}
        result = self.db.execute_query(query, parameters)
        matches = [record["m"] for record in result]
        for match in matches:
            for player_id in player_ids:
                query = "MATCH (p:Player) WHERE id(p) = $player_id CREATE (m)-[:PARTICIPATED]->(p)"
                parameters = {"player_id": player_id}
                self.db.execute_query(query, parameters)
        return matches

    def get_player_matches(self, player_ids):
        query = "MATCH (p:Player)-[:PARTICIPATED]->(m:Match) WHERE id(p) in $player_ids RETURN m"
        parameters = {"player_ids": player_ids}
        result = self.db.execute_query(query, parameters)
        return [record["m"] for record in result]
    
    def get_match(self, match_id):
        query = "MATCH (m:Match) WHERE id(m) = $match_id RETURN m"
        parameters = {"match_id": match_id}
        result = self.db.execute_query(query, parameters)
        if result:
            return result[0]["m"]
        else:
            return None
        
    def close(self):
        self.db.close()