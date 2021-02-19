#!/bin/bash
while [ true ] ;
do
ssh pi@192.168.2.51 << HERE
    ~/scripts/write_to_heartbeat.sh
HERE
sleep 1
done
