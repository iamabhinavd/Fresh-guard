from pymongo import MongoClient

# MongoDB URI (local for now — replace with env var if hosting later)
MONGO_URI = "mongodb://localhost:27017/"

# Create the client
client = MongoClient(MONGO_URI)

# Connect to the database
db = client['perishable_monitoring']

# Access collections
products_collection = db['products']
