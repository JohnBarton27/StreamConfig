#!/bin/bash
while [ true ]
do
    currTime=$(date +%s)
    echo $currTime > ~/heartbeat.txt
    sleep 1
done
