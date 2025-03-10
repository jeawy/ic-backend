import logging

logger = logging.getLogger(__name__)

def error(message):
    return {'error': message}