from os import getenv as e
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

API_ID = e("API_ID", 13691707)
API_HASH = e("API_HASH", "2a31b117896c5c7da27c74025aa602b8")

BOT_TOKEN = e("BOT_TOKEN", "6369035086:AAEQ93w8nqDvQV3re1i9uxE269J_xtKakc0")

mongo = MongoClient("mongodb+srv://Cyberpunk:alpha@cluster0.mxvicxt.mongodb.net/?retryWrites=true&w=majority")
db = mongo.CRED

async def verify(txt): 
    x = await db.credits.find_one({"credits": txt})
    if not x:
        return False
    return True
