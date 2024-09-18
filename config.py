# Safe-repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25713846"))
API_HASH = getenv("API_HASH", "ca57c019f37ab7bf0bd9caead4846c88")
BOT_TOKEN = getenv("BOT_TOKEN", "7520519550:AAE1kW4NqyFcU7_203b-bxh49RAnL64pvvI")
OWNER_ID = int(getenv("OWNER_ID", "5768102179"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://ab123456789ab321:oph3WwTQWbG1FY0h@cluster0.w4ql1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002154322189"))
FORCESUB = getenv("FORCESUB", "-1002154322189")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "") # fill this only if you dont want to force your subscriber to login by this they can use the old method of invite link and can extract from public without login
