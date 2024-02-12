import json
import logging
from database.database import get_products

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

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
