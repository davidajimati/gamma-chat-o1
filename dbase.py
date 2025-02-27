import pymongo

# Load MongoDB connection string from Streamlit secrets (recommended)
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "gamma-chatbot_db"

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]

# Collections
users_collection = db["users"]
messages_collection = db["messages"]
