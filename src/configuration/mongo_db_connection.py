import os
import sys
import pymongo
from src.exception import MyException
from src.logger import logging

class MongoDBClient:
    """MongoDB client connection wrapper."""
    
    def __init__(self, database_name: str = None):
        try:
            mongo_url = os.getenv("MONGODB_URL")
            
            if not mongo_url:
                raise ValueError("MONGODB_URL environment variable not found!")
            
            self.mongo_url = mongo_url
            self.database_name = database_name
            
            # Create connection
            self.client = pymongo.MongoClient(self.mongo_url, serverSelectionTimeoutMS=5000)
            
            # Test connection with ping
            self.client.admin.command('ping')
            logging.info(f"MongoDB connection successful to {database_name}")
            
            # Access database with correct case-sensitive name
            self.database = self.client[database_name]
            
        except Exception as e:
            logging.error(f"MongoDB connection failed: {e}")
            raise MyException(e, sys)
    
    def __getitem__(self, key):
        """Allow accessing collections."""
        return self.database[key]
    
    def close(self):
        """Close MongoDB connection."""
        if self.client:
            self.client.close()
            logging.info("MongoDB connection closed")