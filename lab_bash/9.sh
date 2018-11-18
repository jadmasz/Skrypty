#!/bin/bash
if [ -z $1 ] ; then
	echo podaj sciezke
else
	find "$1" -name "*"
fi
