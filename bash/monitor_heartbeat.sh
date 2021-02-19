#!/bin/bash
while [ true ]
do
    currTime=$(date +%s)
    lastWriteTime=$(cat ~/heartbeat.txt)
    diffInSeconds=$((currTime - lastWriteTime))
    echo $diffInSeconds

    if [[ $diffInSeconds -gt 3600 ]] ; then
        echo "Stream Computer is not on - waiting 30 seconds before trying again..."
	sleep 30
    elif [[ $diffInSeconds -gt 3 ]] ; then
        ~/scripts/go_to_alarm_page.sh
	echo "COMPUTER IS DEAD!!!!"
	exit 1
    else
        sleep 1
    fi
done
