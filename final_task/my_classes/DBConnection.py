import pyodbc


class DBConnection:
    def __init__(self, dbname):
        with pyodbc.connect(f"Driver=SQLite3 ODBC Driver;Database={dbname}") as self.connection:
            self.cursor = self.connection.cursor()

    def create_table(self, table_name, *fields):
        # Construct the SQL query dynamically based on fields and table name
        field_definitions = []

        for field in fields:
            # Assuming field is a tuple like ("column_name", "data_type")
            column_name, data_type = field
            field_definitions.append(f"{column_name} {data_type}")

        # Join all fields into a single string separated by commas
        field_str = ", ".join(field_definitions)
        # print(f"CREATE TABLE IF NOT EXISTS {table_name} ({field_str})")

        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({field_str})")
            self.cursor.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    def select(self, table, fields, where=None):
        fields_string = ', '.join(fields)
        # print(f"SELECT {fields_string} FROM {table} WHERE {where}")
        self.cursor.execute(f"SELECT {fields_string} FROM {table} WHERE {where}")
        result = self.cursor.fetchall()
        return result

    def insert(self, table, **fields):
        fields_keys = tuple(fields.keys())
        fields_values = tuple(fields.values())
        placeholders = ", ".join("?" * len(fields))  # Parameterized values
        query = f"INSERT INTO {table} ({', '.join(fields_keys)}) VALUES ({placeholders})"

        try:
            # Execute the query with the values
            self.cursor.execute(query, fields_values)
            self.connection.commit()  # Commit the changes
        except Exception as e:
            print(f"An error occurred while inserting: {e}")
