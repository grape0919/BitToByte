import logging
import datetime
import os

class Logger():

    mylogger = logging.getLogger("ADMOVE")
    mylogger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(formatter)
    mylogger.addHandler(stream_hander)

    print(os.environ['PYTHONPATH'])

    file_handler = logging.FileHandler(os.path.join(str(os.environ['PYTHONPATH']).replace('"',''),'log','app.log'), encoding="utf-8")
    mylogger.addHandler(file_handler)


    @classmethod
    def info(self, msg):
        self.mylogger.info("["+str(datetime.datetime.now())+"] "+msg)

    @classmethod
    def warn(self, msg):
        self.mylogger.warn("["+str(datetime.datetime.now())+"] "+msg)
        
    @classmethod
    def error(self, msg):
        self.mylogger.error("["+str(datetime.datetime.now())+"] "+msg)
    
    @classmethod
    def debug(self, msg):
        self.mylogger.debug("["+str(datetime.datetime.now())+"] "+msg)
