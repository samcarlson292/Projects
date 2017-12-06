#!/bin/sh

IFS=$'\n'
for line in $(cat song_list.txt)
do
        echo $line
	python twitter_count.py -past $line
done
