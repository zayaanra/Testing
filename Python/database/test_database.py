from typing_extensions import ParamSpec
import database

class Database():
    # Create cursor object for database
    cursor = database.connect()
    records = []
    database.create_table(cursor)

    # Add a record
    def add():
        pass

    # Remove a record
    def rem():
        pass

    # Update a record
    def update():
        pass

    # Retrieve all records
    def get_all():
        pass

    # Retrieve a single record
    def get_one():
        pass


#### we'll add methods here ####

