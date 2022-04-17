import requests
import os
import platform
from plyer import notification

not_connected = b'{"security":{"is_vpn":false}}'
connected = b'{"security":{"is_vpn":true}}'

def notify(message, title):
    if platform.system() == 'Darwin':
        os.system("osascript -e 'display notification \"{}\" with title \"{}\"'".format(message, title))
    else:
        notification.notify(
            title=title,
            message=message)
while True:
    response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=61e6f52fa0424f5aa17d435f93b63637&fields=security")
    if response.content == not_connected:
        notify('se tensó que flipas manin', 'TOR DESCONECTADO')
    elif response.status_code != 200:
        print("[-] Ha habido un error con la petición")
    else:
        print("[+] Conectado correctamente!")
        os.system("sleep 5")
