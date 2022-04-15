from ast import While
import requests


response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=61e6f52fa0424f5aa17d435f93b63637&fields=security")

not_connected = b'{"security":{"is_vpn":false}}'

def new_func(response, not_connected):
    While response.content = not_connected:


if response.content == not_connected:
    print("[-] No conectado a tor")
elif response.status_code != 200:
    print("[-] Ha habido un error con la petición")
else:
    print("[+] Conectado correctamente!")
new_func(response, not_connected)