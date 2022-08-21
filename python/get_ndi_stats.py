import argparse
import hashlib
import os
import requests

parser = argparse.ArgumentParser()
parser.add_argument("input_number")

args = parser.parse_args()

# Read in credentials
cred_file_path = os.path.join(os.path.expanduser("~"), ".credentials")
if not os.path.exists(cred_file_path):
    raise Exception("No credentials file found! Create a .credentials file in your home directory with username and password lines")

with open(cred_file_path, "r") as cred_file:
    lines = [line.strip() for line in cred_file.readlines()]
    username = lines[0].split("=")[-1]
    password = lines[1].split("=")[-1]

ip_mapping = {
    "1": "192.168.2.55",
    "2": "192.168.2.53",
    "3": "192.168.2.52",
    "drum": "192.168.2.54"
}

# Config variables
ip_addr = ip_mapping[args.input_number]
hashed_pw = hashlib.md5(password.encode("utf-8")).hexdigest()

# Use a Session here to perserve cookies
s = requests.Session()

# Authenticate
auth_url = f"http://{ip_addr}/mwapi?method=login&id={username}&pass={hashed_pw}"
r = s.get(auth_url)

import time
# Set channel to given camera
set_channel_url = f"http://{ip_addr}/mwapi?method=set-tally&ext-tally=false"
r = s.get(set_channel_url)
print(f'{r.json()=}')

set_channel_url = f"http://{ip_addr}/mwapi?method=get-tally"
r = s.get(set_channel_url)
print(f'{r.json()=}')



