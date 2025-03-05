from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "simulador_vida_virtual"

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]

npc_collection = database["npcs"]
user_collection = database["users"]
