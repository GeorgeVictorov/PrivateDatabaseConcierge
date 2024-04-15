import logging
from typing import List, Tuple
from database.db import Database


def get_data(query: str) -> Tuple[List[str], List[Tuple]]:
    database = Database()
    conn = database.get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            headers = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            logging.info('Successfully fetched data.')
            return headers, rows
    except Exception as e:
        logging.error(f'An error occurred in get_data function: {str(e)}.')
        return [], []
    finally:
        database.close_database()
