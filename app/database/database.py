import os
import psycopg
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float


async def get_products():
    database_url = os.environ.get("DATABASE_URL")
    query = 'select * from "products"'

    try:
        async with psycopg.AsyncConnection.connect(database_url) as connection:
            async with connection.cursor() as cursor:
                await cursor.execute(query)

                rows = await cursor.fetchall()
    except Exception as e:
        print(f"An error occurred: {e}")

    return None
