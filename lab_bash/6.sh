#!/bin/bash
echo podaj pierwsza liczbe
read num1
echo podaj druga liczbe
read num2
echo podaj dzialanie matematyczne
read znak
if [ "$znak" = "+" ] ; then
	ans=$(( num1 + num2 ))
	echo wynik = $ans
elif [ "$znak" = "-" ] ; then
	ans=$(( num1 - num2 ))
	echo wynik = $ans
elif [ "$znak" = "*" ] ; then
	ans=$(( num1 * num2 ))
	echo wynik = $ans
elif [ "$znak" = "/" ] ; then
	ans=$(( num1 / num2 ))
	echo wynik = $ans
else
	echo zly znak
fi
