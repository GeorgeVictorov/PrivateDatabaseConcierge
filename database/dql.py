import logging
from typing import List, Tuple

from cachetools import TTLCache, cached
from database.db import Database

cache = TTLCache(maxsize=100, ttl=300)


def clear_cached_data():
    """
    Clear cached data from the cache.
    """
    cache.clear()
    logging.info('Cached users config cleared.')


@cached(cache)
def select_data(query: str) -> Tuple[List[str], List[Tuple]]:
    """
    Select data from the database based on the provided query.

    Parameters:
        query (str): The SQL query to execute.

    Returns:
        Tuple[List[str], List[Tuple]]: A tuple containing the column headers and the rows of data.
    """
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
        conn.rollback()
        return [], []
