import requests
import os
import platform
from plyer import notification


api_key = "" #aqui tu api key xd

connected = b'{"city":"null"}'

def notify(message, title):
    if platform.system() == 'Darwin':
        os.system("osascript -e 'display notification \"{}\" with title \"{}\"'".format(message, title))
    else:
        notification.notify(
            title=title,
            message=message)
while True:
    response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=" + api_key +"&fields=city")
    if response.content == connected:
        print("[+] Conectado correctamente!")
        os.system("sleep 5")
    elif response.status_code != 200:
        print("[-] Ha habido un error con la petición")
        os.system("sleep 5")
    else:
        notify('se tensó que flipas manin', 'TOR DESCONECTADO')



