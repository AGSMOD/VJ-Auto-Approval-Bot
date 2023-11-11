# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20919286"))
    API_HASH = getenv("API_HASH", "57b85f72104db3f08f9795b0410eb556")
    BOT_TOKEN = getenv("BOT_TOKEN", "6835125869:AAG2b1HTuDy9Ixq_wawdEyjhyeLelcn8xx0")
    FSUB = getenv("FSUB", "Agsmods")
    CHID = int(getenv("CHID", "-1001955533061"))
    SUDO = list(map(int, getenv("SUDO", "6968528769").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Alax:Alax@cluster0.sdgwcqk.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
