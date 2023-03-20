from os import environ
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(environ.get("APP_ID", "9323694")),
    api_hash= environ.get("API_HASH", "34a0b2551aacd866c3729f7044525353"),
    bot_token= environ.get("TOKEN", "5811423897:AAE8Xk74ILku0bZmx2ZR5l281R8uzIlglWo")
)
