from os import environ 

class Config:
    API_ID = environ.get("API_ID", "18688563")
    API_HASH = environ.get("API_HASH", "48315c25585c23eee6b1f346aad17a68")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6786278075:AAHvQDFYEUk68NtJ95uAHyLKCC02afDLjpo") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5562877717').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
