#!/bin/bash
if [ -z $1 ] ; then
	echo "usage: $0 file.jpg"
else
	rename 's/jpg/png/g' "$1"
fi	
