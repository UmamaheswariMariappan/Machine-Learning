#from us_visa.logger import logging

#logging.info("Starting the demo.py script")

from us_visa.exception import USvisaException
import sys  
from us_visa.logger import logging
import os
from us_visa.pipline.training_pipeline import TrainPipeline

'''
To check the mongo db connection
'''
## print(os.getenv("MONGODB_URL"))

''' to check the pipeline execution'''
obj =TrainPipeline()
obj.run_pipeline()


