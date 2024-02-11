import json
import logging
from database.database import get_products

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Lambda handler started")
    try:
        logger.info("Retrieving products...")
        products = get_products()
        products_list = [product.dict() for product in products]

        logger.info(f"Retrieved {len(products_list)} products")
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "hello world", "products": products_list}),
        }
    except Exception as e:
        logger.error(f"Error in lambda_handler: {e}", exc_info=True)
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"}),
        }
