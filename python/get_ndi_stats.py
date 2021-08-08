import argparse
from datetime import datetime
import hashlib
import json
import os
import time
import requests

parser = argparse.ArgumentParser()
parser.add_argument("input_number")
# parser.add_argument("cam_name")

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
    "2": "192.168.2.53"
}

# Config variables
ip_addr = ip_mapping[args.input_number]
hashed_pw = hashlib.md5(password.encode("utf-8")).hexdigest()

# Use a Session here to perserve cookies
s = requests.Session()

# Authenticate
auth_url = f"http://{ip_addr}/mwapi?method=login&id={username}&pass={hashed_pw}"
r = s.get(auth_url)

# # Set channel to given camera
while True:
    times_file = open("C:\\Users\\John\\times.csv", 'a')
    set_channel_url = f"http://{ip_addr}/mwapi?method=get-summary-info"
    r = s.get(set_channel_url)
    speed = json.loads(r.text)['ethernet']['rx-speed-kbps']
    now = datetime.now()
    times_file.write(f'{now}, {speed}\n')
    print(f'{now}, {speed}')
    times_file.close()

    time.sleep(0.1)
