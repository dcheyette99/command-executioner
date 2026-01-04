from netmiko import ConnectHandler
from datetime import datetime

key_file = "~/.ssh/id_ed25519.pub"

with open("hosts", "r") as file:
    # Read all lines from the file
    hlines = file.readlines()
with open("commands", "r") as file: 
    clines = file.readlines()

# Initialize empty lists to store the hosts and commands
hosts = []
commands = []

# Creating datetime var
now = datetime.now()

# Loop through each line in the file
for hline in hlines:
    hosts.append(hline.strip())
for cline in clines:
    commands.append(cline.strip())

for host in hosts:
    sessionlogfile = f"output/{host}_{now:%Y%m%d-%H%M%S}.txt"
    print(f"Logging into: {host}")
    device = {
            "device_type": "nokia_srl",
            "host": f"{host}",
            "username": "admin",
            "use_keys": True,
            "key_file": key_file,
            "session_log": sessionlogfile,
            "fast_cli": False,
            }
    with ConnectHandler(**device) as net_connect:
        for command in commands:
            print(f"{host}: {command}")
            output = net_connect.send_command(command)
        print(f"{host}: Output generated to {sessionlogfile}")
