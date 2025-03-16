import json
from urllib.request import urlopen

PRIVATE_IP = [
    ("192.168.",),
    ("10.",),
    ("172.", lambda ip: 15 <= int(ip.split('.')[1]) <= 31),
    ("127.",)
]

def is_private_ip(ip):
    for prefix in PRIVATE_IP:
        if ip.startswith(prefix[0]):
            if len(prefix) > 1 and callable(prefix[1]):
                return prefix[1](ip)
            return True
    return False

def data(ip):
    if is_private_ip(ip):
        return ip, "Private", "Local", "Local Network"

    try:
        with urlopen(f"https://rdap.db.ripe.net/ip/{ip}") as response:
            site = response.read().decode('utf-8')
            info = json.loads(site)

        as_number = info.get("autnum", "Unknown")
        country = info.get("country", "Unknown")
        provider = info.get("name", "Unknown")

        if as_number == "Unknown" and "entities" in info:
            as_number = info["entities"][0].get("handle", "Unknown")

        return ip, as_number, country, provider

    except Exception as ex:
        print(f"Ошибка при получении данных для IP {ip}: {ex}")
        return ip, "Error", "Unknown", "Unknown"
