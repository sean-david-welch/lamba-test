import os
import json
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


def get_product_by_id(id: int):
    query = "SELECT * FROM products WHERE id = %s"
    database_url = os.environ.get("DATABASE_URL")

    try:
        with psycopg.connect(database_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id,))

                row = cursor.fetchone()
                if row:
                    return Product(
                        id=row[0], name=row[1], description=row[2], price=row[3]
                    )
                else:
                    return None
    except Exception as e:
        logger.error(
            f"An error occurred while getting product by id: {e}", exc_info=True
        )
        return None


def create_product(product: Product):
    database_url = os.environ.get("DATABASE_URL")
    query = "INSERT INTO products (name, description, price) VALUES (%s, %s, %s)"
    values = (product["name"], product["description"], product["price"])

    try:
        with psycopg.connect(database_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)

                connection.commit()

        return True
    except Exception as e:
        logger.error(f"an error occurred while creating a product: {e}", exc_info=True)
        return None
