# OBS Launcher with Multimonitor Support
On the stream computer's version of Pop_OS!, we seem unable to launch OBS properly unless the third display is disconnected. As manually disabling/disconnecting, launching OBS, and then re-enabling/reconnecting & reconfiguring the layout of the monitors is tedious and silly, we have created a simple shortcut script to automate this action.

## Prerequisites
* Pop!_OS operating system
* `xrandr` command-line tool (can be installed via `sudo apt install xrandr`)
* `notify-send` command-line tool (can be installed via `sudo apt install libnotify-bin`)
* OBS installed and can be launched from command line

## OBS Bash Script
This repository contains a `bash/obs.sh` script. This script disables a specific monitor, launches OBS, waits for it to load, and then re-enables the monitor. 

Be sure to modify the script as necessary with the name(s) of the monitor to disable & your primary monitor. These values can be retrieved by running `xrandr` without any additional commands.

## OBS Desktop File
The `obs.desktop` file that lives in this same directory needs to be symlink'd into the `/usr/share/applications` directory as the root user. Run the following command to make this happen:

```
sudo ln -s /PATH/TO/STREAM_CONFIG/obs/obs.desktop /usr/share/applications/obs.desktop
```

### Proper Pathing
The desktop file needs to have the full, absolute path to an `obs.sh` script that lives in the `bash` directory of this repo as the value of the `Exec` variable. Be sure to update the desktop file if necessary.

Ensure the path to the `Icon` defined in the file is correct - the OBS logo PNG exists in this folder (`obs`) as well.

## Pin to Dash/Launcher
Once you've put the OBS Desktop file in the proper location, you can open the __Application__ view ("Show Applications" from the Launcher or search). Find the (new) "OBS" application - right-click on it and select "Pin to Dash".

Remove any default OBS application(s) that may have already been in the Dash to avoid confusion.