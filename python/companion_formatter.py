import json
import argparse
import os
import pathlib

parser = argparse.ArgumentParser(description="Script used for converting Companion configurations from single-line, "
                                             "minimized JSON files to more a readable/easier to diff format.")

parser.parse_args()

# Load in existing Companion Config file
script_location = pathlib.Path(__file__).parent.absolute()
stream_config_location = "/".join(str(script_location).split("/")[:-1])
filename = os.path.join(stream_config_location, "SUMC.companionconfig")
with open(filename, "r") as old_file:
    config = json.load(old_file)

# Write the JSON back to the file in 'pretty-print' format
with open(filename, "w") as new_file:
    json.dump(config, new_file, indent=4, sort_keys=True)
