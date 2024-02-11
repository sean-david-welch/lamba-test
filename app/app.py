import json
import asyncio
import requests

from database.database import get_products


async def lambda_handler(event, context):

    loop = asyncio.get_event_loop()

    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    products = loop.run_until_complete(get_products())
    products_list = [product.dict() for product in products]

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "hello world", "products": products_list}),
    }
