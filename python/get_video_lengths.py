import argparse
import math
import os
import subprocess

parser = argparse.ArgumentParser(description='Returns the length (in seconds) of each video in the given directory')
parser.add_argument('directory', help='Directory containing one or more video files')
args = parser.parse_args()

os.chdir(args.directory)
files = os.listdir('.')

for video in files:
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", video],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    print(f'{math.ceil(float(result.stdout))} | {video}')
