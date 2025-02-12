import pymysql
import calendar

# Database Manager Class
class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None  

    # Connect to the database
    def connect(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return self.conn.cursor()  
        except pymysql.MySQLError as err:
            print(f"MySQL Connection Error: {err}")
            return None  

    # Disconnect from the database
    def disconnect(self):
        if self.conn:
            self.conn.close()
            self.conn = None  

    # Create a table for the given year and month
    def create_table(self, year, month):
        cursor = self.connect()  
        if not cursor:  
          return False
        try:
            table_name = f"table_{year}_{month:02d}"
            num_days = calendar.monthrange(year, month)[1]
            date_columns = ", ".join([f'`{year}-{month:02d}-{day:02d}` DATE' for day in range(1, num_days + 1)])

            create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                {date_columns}
            );
            '''

            cursor.execute(create_table_query)
            print(f"Table '{table_name}' created successfully.")
            self.disconnect()  
            return True
        except pymysql.MySQLError as err:
            print(f"MySQL Error: {err}")
            self.conn.rollback()  
            self.disconnect()  
            return False 

# Table Manager Class
class TableManager:  
    def __init__(self, db_manager):
        self.db_manager = db_manager

    # Create a table for the given year and month
    def create_table(self, year, month):
        return self.db_manager.create_table(year, month)

# Main Executing Function

if __name__ == "__main__":

    year = 2025
    month = 2

    db_manager = DatabaseManager(host="localhost", user="root", password="suman", database="office")
  
    table_manager = TableManager(db_manager)

    if table_manager.create_table(year, month):
        print("Table operation completed successfully.")
    else:
        print("Table operation failed.")
