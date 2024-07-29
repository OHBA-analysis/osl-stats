import logging
from pkg_resources import DistributionNotFound, get_distribution


# Setup the version
try:
    __version__ = get_distribution("osl-stats").version
except DistributionNotFound:
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound

# Configure logging
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s [%(filename)s:%(lineno)d:%(funcName)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger("osl-stats")
logger.debug("Version %s", __version__)
del logger, logging
