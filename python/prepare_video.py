import argparse
import math
from subprocess import Popen, PIPE, run, STDOUT

parser = argparse.ArgumentParser(description="Prepares video from BMD camera for OBS/Companion")
parser.add_argument("input_video", help="File to be converted.")
parser.add_argument("description", help="Human-readable description of video (for new filename)")
args = parser.parse_args()

original_file_name = args.input_video
description = args.description
new_file_name = f'edited/{description}.mov'

print("Getting length of video...")
result = run(["ffprobe", "-v", "error", "-show_entries",
              "format=duration", "-of",
              "default=noprint_wrappers=1:nokey=1", original_file_name],
             stdout=PIPE,
             stderr=STDOUT)
vid_length = float(result.stdout)
print(vid_length)
extra = vid_length - 30

if extra < 0:
    print("Video is shorter than 30 seconds - will not trim!")
    cut_from_front = math.floor(extra/2)
else:
    cut_from_front = 1

# Add leading zero padding if necessary
if cut_from_front < 10:
    cut_from_front = f'0{cut_from_front}'
start_time = f'00:00:{cut_from_front}'
print(f"Original video was {vid_length} seconds - cutting to 30 seconds, starting at {start_time}.")

print("Removing audio & trimming...")
process = Popen(['ffmpeg', '-i', original_file_name, '-c', 'copy', '-an', new_file_name], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

print("Getting thumbnail...")
thumbnail_process = Popen(['ffmpeg', '-ss', '00:00:00', '-i', new_file_name, '-vframes', '1', '-q:v', '2', '-s', '72x72', f'/home/streaming/Documents/StreamConfig/images/thumbnails/{description}.png'])
thumbnail_stdout, thumbnail_stderr = thumbnail_process.communicate()
