import os
import sys
import pandas as pd
import pymongo
from dotenv import load_dotenv

load_dotenv()

# Read your dataset
csv_path = 'notebook/data.csv'
if not os.path.exists(csv_path):
    print(f"ERROR: Dataset not found at {csv_path}")
    sys.exit(1)

df = pd.read_csv(csv_path)
print(f"Loaded {len(df)} rows from {csv_path}")

# Connect to MongoDB
MONGODB_URL = os.getenv("MONGODB_URL")
if not MONGODB_URL:
    print("ERROR: MONGODB_URL environment variable not set!")
    sys.exit(1)

try:
    client = pymongo.MongoClient(MONGODB_URL, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    print("MongoDB connection successful")
    
    database = client["Proj1"]
    collection = database["Proj1-Data"]
    
    # Clear old data
    deleted = collection.delete_many({})
    print(f"Deleted {deleted.deleted_count} existing records")
    
    # Insert new data
    data = df.to_dict(orient='records')
    result = collection.insert_many(data)
    print(f"Inserted {len(result.inserted_ids)} new records")
    
    # Verify
    count = collection.count_documents({})
    print(f"Total documents now: {count}")
    
    client.close()
    print("MongoDB data insertion completed successfully!")
    
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)