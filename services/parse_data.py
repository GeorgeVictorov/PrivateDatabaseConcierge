import csv
import io
import logging
from datetime import datetime
from typing import List, Tuple

from services.services import hash_file_data


def parse_sql_data(columns: List[str], rows: List[Tuple]) -> str:
    """
    Parse SQL data into a comprehensive format.

    Parameters:
        columns (List[str]): The column names.
        rows (List[Tuple]): The rows of data.

    Returns:
        str: The parsed data in a csv format.
    """
    parsed_data = ''
    parsed_data += ', '.join([f'<b>{col}</b>' for col in columns]) + '\n\n'

    for row in rows[:5]:
        parsed_data += ', '.join(map(str, row)) + '\n'

    if len(rows) > 5:
        parsed_data += f'\n<b>({len(rows) - 5} more rows not shown)</b>'

    return parsed_data


def data_to_csv(columns: List[str], rows: List[Tuple]) -> str | None:
    """
    Convert data to CSV format.

    Parameters:
        columns (List[str]): The column names.
        rows (List[Tuple]): The rows of data.

    Returns:
        str: The CSV data as a string.
    """
    try:
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(columns)
        writer.writerows(rows)
        csv_data = output.getvalue()
        logging.info("Converted sessions history to CSV successfully.")
        return csv_data
    except (io.UnsupportedOperation, csv.Error) as e:
        logging.error(f"Error converting sessions history to CSV: {e}.")
        return None


def generate_filename(data: List[Tuple]) -> str | None:
    """
    Generate a filename for the CSV file.

    Parameters:
        data (List[Tuple]): The rows of data.

    Returns:
        str: The generated filename.
    """
    try:
        data_to_hash = [','.join(map(str, row)) for row in data]
        hashed_data = hash_file_data('\n'.join(data_to_hash))[-4:]
        current_date = datetime.now().strftime('%Y-%m-%d')
        file_name = f'selected_data_{current_date}_{hashed_data}.csv'
        logging.info("Generated filename for sessions history.")
        return file_name
    except Exception as e:
        logging.error(f"Error generating filename for sessions history: {e}.")
        return None
