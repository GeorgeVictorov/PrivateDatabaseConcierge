# Private Database Concierge

Private Database Concierge is a simple tool designed to manage your [PostgreSQL database](https://www.postgresql.org)
directly from Telegram.

With this bot, you can execute SQL queries by sending them directly to the chat.

# Features

* Execute SQL queries via Telegram chat.
* Manage databases seamlessly with three main states:
    1. Start: The initial state.
    2. Select: Querying data and providing a preview, with an option to get a CSV.
    3. DML (Data Manipulation Language): Supports insert, update, and delete operations.

# Usage

1. Send <b>/start</b> to initiate Private Database Concierge.
2. Use <b>/dql</b> to enter Data Query Language (DQL) mode.
3. Use <b>/dml</b> to enter Data Manipulation Language (DML) mode.

# Technologies Used

The project employs [aiogram](https://github.com/aiogram/aiogram) and [psycopg](https://github.com/psycopg/psycopg) for
its core functionalities.

# Overview
