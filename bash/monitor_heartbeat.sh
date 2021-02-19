#!/bin/bash
echo "Starting heartbeat monitor..." > /home/pi/monitor_heartbeat.log
while [ true ]
do
    currTime=$(date +%s)
    lastWriteTime=$(cat /home/pi/heartbeat.txt)
    diffInSeconds=$((currTime - lastWriteTime))
    echo $diffInSeconds >> /home/pi/monitor_heartbeat.log

    if [[ $diffInSeconds -gt 10 ]] ; then
        echo "Stream Computer is not on - waiting 30 seconds before trying again..." >> /home/pi/monitor_heartbeat.log
	sleep 30
    elif [[ $diffInSeconds -gt 3 ]] ; then
        /home/pi/scripts/go_to_alarm_page.sh
	echo "COMPUTER IS DEAD!!!!" >> /home/pi/monitor_heartbeat.log
	sleep 10
    else
        sleep 1
    fi
done
