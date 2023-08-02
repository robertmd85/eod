import asyncpg
from json import dumps as json_dumps
from asyncpg import Connection


def connect_to_postgres() -> Connection:
    connection = asyncpg.connect(
        host="localhost",
        database="stock_data",
        user="postgres",
        password="admin"
    )
    print("Connected to the PostgreSQL database successfully!")
    return connection


def insert_json_data(table: str, data: dict) -> None:
    try:
        connection = connect_to_postgres()
        columns = ', '.join(data.keys())
        placeholders = ', '.join(f'${i+1}' for i in range(len(data)))
        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        connection.execute(query, *data.values())
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        connection.close()
