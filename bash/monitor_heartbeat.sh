#!/bin/bash
while [ true ]
do
    currTime=$(date +%s)
    lastWriteTime=$(cat ~/heartbeat.txt)
    diffInSeconds=$((currTime - lastWriteTime))
    echo $diffInSeconds

    if [[ $diffInSeconds -gt 3 ]] ; then
        ~/scripts/go_to_alarm_page.sh
	echo "COMPUTER IS DEAD!!!!"
	exit 1
    fi

    sleep 1
done
