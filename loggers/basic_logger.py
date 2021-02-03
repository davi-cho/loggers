from sys import stdout
from loguru import logger as loguru_logger


def crear_logger():
	loguru_logger.remove()
	loguru_logger.add(
		stdout,
		colorize=True,
		level="INFO",
		format="<light-cyan>{time:MM-DD-YYYY HH:mm:ss}</light-cyan> | \
		<light-green>{level}</light-green>: \
		<light-white>{message}</light-white>"
	)
	loguru_logger.add(
		'.logs/errors.log',
		colorize=True,
		level="ERROR",
		rotation="200 MB",
		catch=True,
		format="{time:MM-DD-YYYY HH:mm:ss} | {level}: {message}"
	)
	return loguru_logger


basic_logger = crear_logger()