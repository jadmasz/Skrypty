#!/bin/bash

echo Podaj nowe haslo
read haslo
echo Podaj haslo
read input
if [ "$haslo" = "$input" ]; then
	echo zamek owarty
else
	echo zle haslo	
fi
