"""
app.py
Main entry point for the Flight Booking System Python application.
Connects to MySQL and executes all 10 SQL queries.

Team Name: [Your Team Name]
Student Numbers: [4395764, ...]
File: app.py
"""

from db_connection import create_connection, execute_query, close_connection
from queries import QUERIES


def main():
    """Main function: connect to DB and run all queries."""

    print("=" * 70)
    print(" FLIGHT BOOKING SYSTEM — DATABASE QUERY DEMO")
    print(" CSC312 Database Systems — Practical Assignment 2")
    print("=" * 70)

    # Step 1: Connect to the database
    connection = create_connection()
    if not connection:
        print("\n✗ Could not connect to the database. Check your .env file.")
        return

    # Step 2: Run each query in order
    try:
        for title, query in QUERIES.items():
            execute_query(connection, query, title=title)
            input("\nPress Enter to continue to the next query...")

    except KeyboardInterrupt:
        print("\n\n⚠ Execution interrupted by user.")

    finally:
        # Step 3: Always close the connection
        close_connection(connection)


if __name__ == "__main__":
    main()