import sys

from us_visa.exception import USvisaException
from us_visa.logger import logging

import os
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None: #If no MongoDB client exists, a new one is created.
                mongo_db_url = os.getenv(MONGODB_URL_KEY) #Uses os.getenv to fetch the MongoDB URL from the environment variable defined by MONGODB_URL_KEY.
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")#Ensures the MongoDB URL is set; otherwise, raises an exception.
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)#Initializes the MongoDB client with a secure connection using the certificate (ca).
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name #Stores the connection and database for instance-level use.
            logging.info("MongoDB connection succesfull") #Logs a success message upon a successful connection.
        except Exception as e:
            raise USvisaException(e,sys) #If any error occurs, it raises a custom USvisaException with the original exception and system traceback for debugging.