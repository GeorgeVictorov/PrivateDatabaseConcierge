import logging

import psycopg
from config_data.config import load_config


class Database:
    """
    Singleton class for managing a database connection.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Create a new instance if it doesn't already exist.

        Returns:
            Database: The Database instance.
        """
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """
        Initialize the Database instance.
        """
        if not self._initialized:
            self.config = load_config()
            self.db_connection = None
            self._initialize_connection()
            self._initialized = True

    def _initialize_connection(self):
        """
        Initialize the database connection.
        """
        if self.db_connection is None:
            try:
                logging.info('Creating a new database connection...')
                self.db_connection = psycopg.connect(
                    dbname=self.config.db.database,
                    user=self.config.db.db_user,
                    password=self.config.db.db_password,
                    host=self.config.db.db_host
                )
                logging.info('Database connection created successfully.')
            except psycopg.Error as e:
                logging.error(f'Error creating database connection: {e}.')

    def get_connection(self):
        """
        Get the database connection.

        Returns:
            psycopg.connection: The database connection.
        """
        if self.db_connection is not None:
            logging.info('Reusing existing database connection...')
            return self.db_connection
        else:
            self._initialize_connection()
            return self.db_connection

    def close_database(self):
        """
        Close the database connection.
        """
        if self.db_connection:
            try:
                self.db_connection.close()
                logging.info('Database connection closed.')
            except Exception as e:
                logging.error(f'Error closing database connection: {e}.')
        else:
            logging.warning('No open database connection to close or connection is already closed.')
