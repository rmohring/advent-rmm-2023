#!/bin/bash
# call it with 
# ./1-1.sh input1-1.dat
# or
# bash 1-1.sh input1-1.dat
sum=0
while read i
do
  # double the string to handle the case where there's just one number
  # get rid of the remaining letters and get the first and last character
  j=$(echo $i$i | sed 's/[^0-9]*//g' | sed 's/\(.\).*\(.\)/\1\2/')
  sum=$(( sum + j ))
done < $1

echo $sum
