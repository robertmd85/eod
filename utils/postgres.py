import asyncpg
from json import dumps as json_dumps
from asyncpg import Connection


async def connect_to_postgres() -> Connection:
    connection = await asyncpg.connect(
        host="localhost",
        database="stock_data",
        user="postgres",
        password="admin"
    )
    print("Connected to the PostgreSQL database successfully!")
    return connection


async def insert_json_data(table: str, data: dict) -> None:
    try:
        connection = await connect_to_postgres()
        columns = ', '.join(data.keys())
        placeholders = ', '.join(f'${i+1}' for i in range(len(data)))
        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        await connection.execute(query, *data.values())
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        await connection.close()
