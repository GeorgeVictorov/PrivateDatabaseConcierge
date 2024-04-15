import logging

from database.db import Database


def change_data(query: str) -> str:
    """
    Execute a DML query and return a message indicating success or failure.

    Parameters:
        query (str): The DML query to execute.

    Returns:
        str: A message indicating success or failure.
    """
    database = Database()
    conn = database.get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
            logging.info('Successfully changed data.')
            return 'Data successfully changed.'
    except Exception as e:
        logging.error(f'An error occurred in change_data function: {str(e)}.')
        conn.rollback()
        return f'Failed to change data: {e}'
