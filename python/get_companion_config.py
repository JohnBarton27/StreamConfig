import glob
from os.path import expanduser
import os
import pathlib
import shutil

download_location = os.path.join(expanduser("~"), "Downloads", "*.companionconfig")

comp_configs = glob.glob(download_location)
most_recent_config = max(comp_configs, key=os.path.getctime)

cwd = pathlib.Path(__file__).parent.absolute()
target_dir = "/".join(str(cwd).split("/")[:-1])

shutil.move(most_recent_config, os.path.join(target_dir, "SUMC.companionconfig"))

import companion_formatter
