import logging


def setup_logging():
    """Configures logging for the application."""
    logging.basicConfig(
        filename='user_registration.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
