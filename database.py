import sqlite3
from sqlite3 import Error


class Database:

    # Path to the database
    path = "database/database.sqlite"

    # Query to create the score table
    create_score_table = """
        CREATE TABLE IF NOT EXISTS score (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        score INTEGER
        );
        """

    ### FUNCTIONS ###
    def create_connection(self, path):
        """Create a database connection to a SQLite database.
        return: Connection object or None

        Args:
            - path (str): The path to the SQLite database.
        """

        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    def execute_query(self, connection, query):
        """Execute a query on the database.

        Args:
            - connection (sqlite3.Connection): The connection to the database.
            - query (str): The query to execute.
        """

        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def create_new_score(self, connection, score):
        """Create a new score in the database.

        Args:
            - connection (sqlite3.Connection): The connection to the database.
            - score (int): The score to insert into the database.
        """

        cursor = connection.cursor()
        try:
            cursor.execute(
                f"""
                INSERT INTO 
                score (date, score) 
                VALUES 
                (date('now'), {score});"""
            )
            connection.commit()
            print("New score created")
        except Error as e:
            print(f"The error '{e}' occurred")

    def clear_scores(self, connection):
        """Clear all scores from the database.

        Args:
            - connection (sqlite3.Connection): The connection to the database.
        """

        cursor = connection.cursor()
        try:
            cursor.execute(
                f"""
                DELETE FROM score;
                """
            )
            connection.commit()
            print("Scores cleared")
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_read_query(self, connection):
        """Execute a read query on the database.
        return: The result of the query.

        Args:
            - connection (sqlite3.Connection): The connection to the database.
        """

        cursor = connection.cursor()
        result = None
        query = "SELECT * FROM score ORDER BY score DESC LIMIT 15"
        score_list = []
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e:
            print(f"The error '{e}' occurred")

        if result != None:
            for entry in result:
                score_list.append(entry)
            return score_list
