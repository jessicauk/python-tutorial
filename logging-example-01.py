import logging

logging.warning("watch out!")
# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="lumberjack.log", level=logging.ERROR, format=LOG_FORMAT, filemode="w")
logger = logging.getLogger()

# Test the logger
logger.info("Our first message")

print(logger.level)

# Test messages

logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!")