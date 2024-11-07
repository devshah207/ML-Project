## log all the info (of execution) in some files which help us in tracking errors, changes made etc

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

    ## so from now onwards whenever we import login and login.info and then write out any print message, then it is going to use this kind of basic config. 
    ## so now on whenever an exception is raised we will use login and login.info to put that message into file.
)

# if __name__ == "__main__":
#     logging.info("Logging has started")