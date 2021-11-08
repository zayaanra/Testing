import mysql.connector, json

# This function connect to the database.
def connect():
    db = mysql.connector.connect(
        db="mydb",
        host="localhost",
    )
    return db.cursor()

# This function creates a table if it does not already exist.
def create_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS Food (fruit VARCHAR(2048), color VARCHAR(2048), id int PRIMARY KEY AUTO_INCREMENT")

# This function inserts a record into the table "Food".
def insert_record(record, cursor):
    data = json.loads(record)
    cursor.execute("INSERT INTO Food(fruit, color) VALUES (?, ?)", (data["fruit"], data["color"]))

# This function retrieves all records from a database
def retrieve_all(cursor):
    cursor.execute("SELECT * FROM Food")
    json_obj = []
    for record in cursor:
        json_obj.append({"fruit":record[0], "color":record[1]})
    return json_obj

# This function retrieves a single record from a database
def retrieve_single(cursor, id):
    cursor.execute("SELECT COUNT(1) FROM Food WHERE id = %s" % id)
    if not cursor.fetchone()[0]:
        return False
    cursor.execute("SELECT * FROM Food WHERE id = %s" % id)
    return cursor.fetchall()

# This function updates a record in the database.
def update_record(cursor, new_record, id):
    cursor.execute("SELECT COUNT(1) FROM Food WHERE id = %s" % id)
    if not cursor.fetchone()[0]:
        return False
    cursor.execute("UPDATE Food SET fruit = %s WHERE id = %s" % (new_record["fruit"], id))
    cursor.execute("UPDATE Food SET color = %s WHERE id = %s" % (new_record["color"], id))

# This function deletes a record from the database.
def delete_record(cursor, id):
    cursor.execute("SELECT COUNT(1) FROM Food WHERE id = %s" % id)
    if not cursor.fetchone()[0]:
        return False
    cursor.execute("DELETE FROM Food WHERE id = %s" % id)