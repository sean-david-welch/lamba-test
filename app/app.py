import json
import logging
from database.database import get_products, get_product_by_id, create_product

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_products_handler(event, context):
    try:
        products = get_products()
        products_list = [product.model_dump() for product in products]

        return {
            "statusCode": 200,
            "body": json.dumps(
                {"message": "products fetched from postgres", "products": products_list}
            ),
        }

    except Exception as e:
        logger.error(f"Error in lambda_handler: {e}", exc_info=True)
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"}),
        }


def get_product_id_handler(event, context):
    try:
        id = event["pathParameters"]["id"]
        product = get_product_by_id(id)

        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": "product fetch successfully",
                    "product": product.model_dump(),
                }
            ),
        }

    except Exception as e:
        logger.error(f"Error in get_product_id_handler: {e}", exc_info=True)
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"}),
        }


def create_product_handler(event, context):
    try:
        product = event["product"]
        create_product(product)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "product created successfully"}),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(
                {"message": f"error occurred while creating product: {e}"}
            ),
        }
