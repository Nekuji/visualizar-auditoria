import logging
import requests
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        requests.post(event["url"])
        logger.info("SUCCESS: Request on url " + event["url"])
    except:
        logger.error("ERROR: Unexpected error occurred")
        logger.error(sys.exc_info()[0])
