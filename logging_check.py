import logging

logging.basicConfig(
    filename='app.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',  
    filemode='a' 
)

logging.info("Hello, World!")

logging.debug("This is a debug message")
logging.warning("This is a warning message")
logging.error("This is an error message")

# Good practice
logging.shutdown()