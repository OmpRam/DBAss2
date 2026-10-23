"""
test_connection.py
Temporary script to verify the MySQL connection works.
Delete this file once you've confirmed the connection.
"""

from db_connection import create_connection, close_connection

conn = create_connection()
if conn:
    print("✓ Connection works!")
    close_connection(conn)
else:
    print("✗ Connection failed.")
    print("  Check:")
    print("   1. .env file has correct credentials")
    print("   2. MySQL server is running and reachable")
    print("   3. DB_PORT is a number (e.g. 3306), not an IP address")
    print("   4. SSL settings match server requirements")