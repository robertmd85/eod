import asyncpg
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


async def insert_json_data(connection :str, table :str, json_data: dict) -> None:
    try:
        query = f"INSERT INTO { table } (data) VALUES ($1)"
        await connection.execute(query, json_data)
        print("JSON data inserted successfully!")
    except Exception as e:
        print(f"Error inserting JSON data: {e}")


async def insert_data() -> None:
    connection = await connect_to_postgres()
    json_data = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]
    await insert_json_data(connection, json_data)
    await connection.close()
