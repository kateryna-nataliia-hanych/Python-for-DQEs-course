import pyodbc
from datetime import datetime
# print(pyodbc.drivers())
class DBConnection:
    def __init__(self, dbname):
        with pyodbc.connect(f"Driver=SQLite3 ODBC Driver;Database={dbname}") as self.connection:
            self.cursor = self.connection.cursor()

    def create_table(self, table_name,  *fields):
        # Construct the SQL query dynamically based on fields and table name
        field_definitions = []

        for field in fields:
            # Assuming field is a tuple like ("column_name", "data_type")
            column_name, data_type = field
            field_definitions.append(f"{column_name} {data_type}")

        # Join all fields into a single string separated by commas
        field_str = ", ".join(field_definitions)

        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({field_str})")
            self.cursor.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    def insert(self, table_name,  **fields):
        table_fields = tuple(fields.keys())
        table_values = tuple(fields.values())
        try:
            self.cursor.execute(f"INSERT INTO {table_name} {table_fields} VALUES {table_values}")
            self.cursor.commit()
            print(f"Next values {table_values} were inserted to the table '{table_name}' successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def select(self, field, table):
        self.cursor.execute(f"SELECT {field} FROM {table}")
        result = self.cursor.fetchall()
        print(result)

    def check_duplication(self, table_name, groupby, **fields):

        field_conditions = [f"{key} = ?" for key in fields.keys()]
        table_fields = ', '.join(fields.keys())
        table_values = tuple(fields.values())
        print(f"SELECT * FROM {table_name} WHERE  " + " AND ".join(field_conditions) + f" GROUP BY {', '.join(groupby)}")
        try:
            result = self.cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE  " + " AND ".join(field_conditions) + f" GROUP BY {table_fields}", table_values)
            if result.fetchone() is None:
                print("No duplication")
                return False
            else:
                print("Duplicate found!")
                return True

        except Exception as e:
            print(f"An error occurred: {e}")


