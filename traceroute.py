import os
import re

def traceroute(target):
    ip_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    command = f"tracert {target}"

    print(f"Выполняется команда: {command}")
    with os.popen(command) as process:
        output = process.read()

    ips = ip_pattern.findall(output)
    print(f"Найденные IP-адреса: {ips}")
    return ips