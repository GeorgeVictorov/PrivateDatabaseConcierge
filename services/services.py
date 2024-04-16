import hashlib
import logging
import sys

from database.db import Database


def hash_file_data(data: str) -> str:
    """
    Hash the provided file data using SHA-256 algorithm.
    """
    try:
        file_hash = hashlib.sha256()
        for line in data:
            file_hash.update(line.encode('utf-8'))
        logging.info('Hashed file data successfully')
        return file_hash.hexdigest()
    except Exception as e:
        logging.error(f"Error hashing file data: {e}")


def sigterm_handler():
    """
    Handle the SIGTERM signal.
    """
    db_instance = Database()
    try:
        logging.info('SIGTERM received. Shutting down...')
        db_instance.close_database()
        sys.exit(0)
    except Exception as e:
        logging.error(f'Error in sigterm_handler: {e}')
        sys.exit(1)


def sigint_handler():
    """
     Handle the SIGINT signal.
    """
    db_instance = Database()
    try:
        logging.info('Received SIGINT signal. Shutting down...')
        db_instance.close_database()
        sys.exit(0)
    except Exception as e:
        logging.error(f'Error in sigint_handler: {e}')
        sys.exit(1)
