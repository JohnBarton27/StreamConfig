#!/bin/bash
PREV_PAGE="`cat ~/prev_page.txt`"
curl -X GET http://192.168.2.51:8000/press/bank/$PREV_PAGE/32
