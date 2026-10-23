"""
db_connection.py
Handles MySQL database connection and query execution.

Team Name: [Your Team Name]
Student Numbers: [4395764, ...]
"""

import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG
from tabulate import tabulate


def create_connection():
    """
    Create and return a MySQL database connection.
    Returns None if the connection fails.
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print(f"✓ Connected to MySQL database: {DB_CONFIG['database']}")
            return connection
    except Error as e:
        print(f"✗ Error connecting to MySQL: {e}")
        return None


def execute_query(connection, query, params=None, title="Query Result"):
    """
    Execute a SELECT query and print results in a formatted table.
    """
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query, params or ())
        results = cursor.fetchall()

        print(f"\n{'=' * 70}")
        print(f" {title}")
        print(f"{'=' * 70}")

        if results:
            print(tabulate(results, headers="keys", tablefmt="grid"))
            print(f"\n→ {len(results)} row(s) returned.")
        else:
            print("No results found.")

        return results

    except Error as e:
        print(f"✗ Query failed: {e}")
        return None
    finally:
        cursor.close()


def close_connection(connection):
    """Close the MySQL connection if it is open."""
    if connection and connection.is_connected():
        connection.close()
        print("\n✓ MySQL connection closed.")