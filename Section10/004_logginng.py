from logging import basicConfig,getLogger,DEBUG,INFO,WARNING,ERROR,CRITICAL
path='Section10/log001.log'
basicConfig(filename=path,filemode='w',level=DEBUG,format=' %(asctime)s [%(filename)-4s %(lineno)d]  %(levelname)-4s   :   %(message)s ',datefmt='%Y_%m_%d [%H : %M : %S]')
logger=getLogger(__name__)

logger.debug("debug")
logger.info("hello")
logger.warning("warning")
logger.error("Error")
logger.critical("Critical")