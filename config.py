from os import environ 

class Config:
    API_ID = environ.get("API_ID", "18694811")
    API_HASH = environ.get("API_HASH", "2257d0135b9034aa25b307ba3c47f004")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7137840331:AAG_UXhuVdd-Ewh4Jub5c7B9V0A-kVmLvfs") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://theghost:TheGHOST1123@youtubedownloader.kn2hbxl.mongodb.net/?retryWrites=true&w=majority&appName=YoutubeDownloader
")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1248187876').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
