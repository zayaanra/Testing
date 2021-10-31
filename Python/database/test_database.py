import database

class Database():
    # Create cursor object for database
    cursor = database.connect()
    records = []
    database.create_table(cursor)

    # Add a record
    def add(self, record):
        database.insert_record(record, self.cursor)

    # Remove a record
    def rem(self, id):
        database.delete_record(self.cursor, id)

    # Update a record
    def update(self, record, id):
        return database.update_record(self.cursor, record, id)

    # Retrieve all records
    def get_all(self):
        return database.retrieve_all(self.cursor)

    # Retrieve a single record
    def get_one(self, id):
        return database.retrieve_single(self.cursor, id)


db = Database()
rec1 = '{"food":"orange","color":"orange"}'
rec2 = '{"food":"apple","color":"red"}'
rec3 = '{"food":"watermelon","color":"green"}'

update1 = '{"food":"banana","color":"yellow"}'

db.add(rec1); db.add(rec2); db.add(rec3) # Insertion
data = db.get_all(); print(data) # Retrieve All

db.update(update1, 1) # Update (if record exists)
data = db.get_all(); print(data) # Retrieve All

db.update(update1, 5) # Update (if record does not exist)
data = db.get_all(); print(data) # Retrieve All

db.rem(2) # Delete (if record exists)
data = db.get_all(); print(data) # Retrieve All

db.rem(29) # Delete (if record does not exist)
data = db.get_all(); print(data) # Retrieve All

data = db.get_one(3) # Retrieve single (if record does exist)
print(data)

data = db.get_one(-5) # Retrieve single (if record does not exist)
print(data)

