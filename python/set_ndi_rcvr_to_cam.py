import argparse
import hashlib
import os
import requests
import urllib.parse

parser = argparse.ArgumentParser()
parser.add_argument("input_number")
parser.add_argument("cam_name")

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
    "3": "192.168.2.52"
}

ndi_mapping = {
    "PIANO": "SANCTUARY CAMERA 2 - BMPCC (#02 (A405200417010))",
    "PTZ2": "CAM 200",
    "PTZ1": "Cam 201",
    "DRUM": "SANCTUARY PRO7 (#00 (A405200220039))",
    "PROPRES": "SUNTREES-IMAC.LOCAL (Sanctuary ProP New)"
}

# Config variables
ip_addr = ip_mapping[args.input_number]
cam_name = ndi_mapping[args.cam_name]
hashed_pw = hashlib.md5(password.encode("utf-8")).hexdigest()

# Use a Session here to perserve cookies
s = requests.Session()

# Authenticate
auth_url = f"http://{ip_addr}/mwapi?method=login&id={username}&pass={hashed_pw}"
r = s.get(auth_url)

# Set channel to given camera
if args.input_number == "1" and args.cam_name == "PTZ1":
    set_channel_url = f"http://{ip_addr}/mwapi?method=set-channel&ndi-name=true&name={urllib.parse.quote('CAM 201 (Chan2, 192.168.2.201)')}"
elif args.input_number == "2" and args.cam_name == "PTZ2":
    set_channel_url = f"http://{ip_addr}/mwapi?method=set-channel&ndi-name=true&name={urllib.parse.quote('CAM 200 (Chan1, 192.168.2.200)')}"
else:
    set_channel_url = f"http://{ip_addr}/mwapi?method=set-channel&ndi-name=true&name={urllib.parse.quote(cam_name)}"
print(set_channel_url)
r = s.get(set_channel_url)
print(r)
print(r.json())
