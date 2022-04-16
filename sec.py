import requests
import os

not_connected = b'{"security":{"is_vpn":false}}'
connected = b'{"security":{"is_vpn":true}}'

while True:
    response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=61e6f52fa0424f5aa17d435f93b63637&fields=security")
    if response.content == not_connected:
        print("[-] No conectado a tor")
    elif response.status_code != 200:
        print("[-] Ha habido un error con la petición")
    else:
        print("[+] Conectado correctamente!")
        os.system("sleep 5")
        
        
