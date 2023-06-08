#!/bin/bash

# Replace "Display1" with the actual name of your display.
# You can find this by running the 'xrandr' command with no arguments.
DISPLAY_NAME="HDMI-2"
PRIMARY_DISPLAY_NAME="HDMI-1"

# Disable the display.
xrandr --output $DISPLAY_NAME --off

# Launch OBS and wait for it to load.
# Replace "obs" with the actual command you use to launch OBS if it's different.
obs &

# Let's assume OBS takes 10 seconds to load. Adjust this time if needed.
sleep 7

# Re-enable the display.
# Replace "1920x1080" with the correct resolution for your display.
# If the display is not positioned to the right of another display, you might want to adjust "--right-of".
# You can check your current settings with 'xrandr' command to understand the layout.
xrandr --output $DISPLAY_NAME --auto --left-of $PRIMARY_DISPLAY_NAME

