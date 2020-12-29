#! /bin/bash
SESSION_FILE=~/.dyalog/robot.dlf
rm -f $SESSION_FILE
export RIDE_INIT=HTTP:*:4999
export LOG_FILE=$SESSION_FILE
dyalog
