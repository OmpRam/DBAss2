"""
config.py
Loads database credentials from the .env file.

Team Name: [Your Team Name]
Student Numbers: [4395764, ...]
"""

import os
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()

# Database configuration dictionary
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "flight_booking_system"),
    "port": int(os.getenv("DB_PORT", 3306)),
    # SSL settings — server requires encrypted connection
    "ssl_disabled": False,
}