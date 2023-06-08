#!/bin/bash

# Replace "Display1" with the actual name of your display.
# You can find this by running the 'xrandr' command with no arguments.
DISPLAY_NAME="HDMI-2"
PRIMARY_DISPLAY_NAME="HDMI-1"

# Check if OBS is already running
if pgrep -x "obs" > /dev/null
then
    notify-send -u normal -t 5000 "" "OBS is already running!"
    exit 1
fi

# Display a message to the user
notify-send -u normal -t 10000 "Do not be afraid!" "Monitors may turn on & off automatically."

sleep 3

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

