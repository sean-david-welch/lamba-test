import os
import logging
import psycopg

from pydantic import BaseModel

logger = logging.getLogger()


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float


def get_products():
    query = 'SELECT * FROM "products"'
    database_url = os.environ.get("DATABASE_URL")

    try:
        with psycopg.connect(database_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)

                rows = cursor.fetchall()
                return [
                    Product(id=row[0], name=row[1], description=row[2], price=row[3])
                    for row in rows
                ]
    except Exception as e:
        logger.error(f"An error occurred in get_products: {e}", exc_info=True)
        return None
