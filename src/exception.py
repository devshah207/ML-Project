## sys module in python provides various func. and variables used to manipulate diff. parts of Py RTE
# from src.logger import logging
import sys

def error_message_detail(error,error_detail:sys):
    ## returns 3 things. First two are of no use. But third will give info like on which file error occured, on which line no etc.
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    

# if __name__ == "__main__":

#     try: 
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by Zero Error")
#         raise CustomException(e,sys)
        