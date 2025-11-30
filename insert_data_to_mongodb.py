import os
import sys
import pandas as pd
import pymongo
from pymongo.errors import ConnectionFailure
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
    client = pymongo.MongoClient(MONGODB_URL, serverSelectionTimeoutMS=10000)
    client.admin.command('ping')
    print("MongoDB connection successful")
    
    database = client["Proj1"]
    collection = database["Proj1-Data"]
    
    # Clear old data
    deleted = collection.delete_many({})
    print(f"Deleted {deleted.deleted_count} existing records")
    
    # Insert new data in batches
    print("Inserting new data in batches...")
    chunk_size = 10000
    total_inserted = 0
    for i in range(0, len(df), chunk_size):
        chunk = df.iloc[i:i+chunk_size]
        data = chunk.to_dict(orient='records')
        result = collection.insert_many(data)
        total_inserted += len(result.inserted_ids)
        print(f"  Inserted batch {i//chunk_size + 1}, {len(result.inserted_ids)} records. Total inserted: {total_inserted}")

    print(f"Finished inserting {total_inserted} new records.")
    
    # Verify
    count = collection.count_documents({})
    print(f"Total documents now: {count}")
    
except ConnectionFailure as e:
    print(f"ERROR: MongoDB connection failed: {e}")
    sys.exit(1)
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)
finally:
    if 'client' in locals() and client:
        client.close()
        print("MongoDB connection closed.")