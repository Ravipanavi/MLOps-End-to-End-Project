import os
import sys
import pandas as pd
import numpy as np
from typing import Optional

from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME, DATA_INGESTION_COLLECTION_NAME
from src.exception import MyException
from src.logger import logging

class Proj1Data:
    """A class to export MongoDB records as a pandas DataFrame."""

    def __init__(self) -> None:
        """Initializes the MongoDB client connection."""
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
            logging.info(f"Proj1Data initialized - connected to {DATABASE_NAME}")
        except Exception as e:
            logging.error(f"Failed to initialize Proj1Data: {e}")
            raise MyException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str = DATA_INGESTION_COLLECTION_NAME) -> pd.DataFrame:
        """
        Exports an entire MongoDB collection as a pandas DataFrame.

        Parameters:
        ----------
        collection_name : str
            The name of the MongoDB collection to export.

        Returns:
        -------
        pd.DataFrame
            DataFrame containing the collection data.
        """
        try:
            logging.info(f"Accessing collection: {collection_name}")
            
            # Access collection
            collection = self.mongo_client.database[collection_name]
            
            # Count documents
            count = collection.count_documents({})
            logging.info(f"Total documents in '{collection_name}': {count}")
            
            if count == 0:
                logging.warning(f"Collection '{collection_name}' is EMPTY! No data to fetch.")
                return pd.DataFrame()
            
            # Fetch all documents
            logging.info("Fetching data from MongoDB...")
            records = list(collection.find({}))
            df = pd.DataFrame(records)
            
            logging.info(f"Data fetched successfully - Shape: {df.shape}")
            
            # Remove MongoDB's internal _id column
            if "_id" in df.columns:
                df = df.drop(columns=["_id"])
                logging.info("Removed '_id' column")
            
            # Replace 'na' strings with NaN
            df.replace({"na": np.nan}, inplace=True)
            
            logging.info(f"Final DataFrame shape: {df.shape}")
            return df

        except Exception as e:
            logging.error(f"Error exporting collection: {e}")
            raise MyException(e, sys)