import logging


def configure_logging(app):
    # Remove the default Flask logger handlers
    del app.logger.handlers[:]

    # Create a new logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create a handler
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    # Create a formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    # Set the logger for the Flask app
    app.logger.addHandler(handler)
