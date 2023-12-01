#!/bin/bash
sum=0
while read t
do
  #echo "======================"
  #echo $t
  #echo "----------"
  min_idx=999
  ctr=1
  for patt in one two three four five six seven eight nine
  do
    temp=${t%%$patt*}
    #echo $patt ${#temp}
    idx=${#temp}
    if [ "$idx" -lt "$min_idx" ]; then
       min_idx=$idx
       keep_patt=$patt
       keep_ctr=$ctr
    fi
    temp=${t%%$ctr*}
    #echo $patt ${#temp}
    # this bit searches for digits also and if a digit is lower, don't do anything
    idx=${#temp}
    if [ "$idx" -lt "$min_idx" ]; then
       min_idx=$idx
       keep_patt="JUNKPATTERN"
       keep_ctr=$ctr
    fi
    ctr=$((ctr+1))
  done
  #echo 'REGEX'
  #echo "s/$keep_patt/$keep_ctr/"
  t=$(echo $t | sed "s/$keep_patt/$keep_ctr/")
  #echo $t
  
  # Now, reverse the string and the text-numbers and do it again
  # Could I refactor this into a single loop? Of course. Am I going to?
  # No, no I am not.
  t_rev=$(echo $t | rev)
  ctr=1
  min_idx=999
  #echo $t_rev
  for patt in one two three four five six seven eight nine
  do
    patt_rev=$(echo $patt | rev)
    temp=${t_rev%%$patt_rev*} 
    #echo $patt_rev ${#temp}
    idx=${#temp}
    if [ "$idx" -lt "$min_idx" ]; then
       min_idx=$idx
       keep_patt=$patt_rev
       keep_ctr=$ctr
    fi
    # this bit searches for digits also and if a digit is lower, don't do anything
    temp=${t_rev%%$ctr*}
    #echo $patt ${#temp}
    idx=${#temp}
    if [ "$idx" -lt "$min_idx" ]; then
       min_idx=$idx
       keep_patt="JUNKPATTERN"
       keep_ctr=$ctr
    fi
    ctr=$((ctr+1))
  done
  #echo 'REGEX'
  #echo "s/$keep_patt/$keep_ctr/"
  t_rev=$(echo $t_rev | sed "s/$keep_patt/$keep_ctr/")
  final=$(echo $t_rev | rev)
  #echo $final

  # double the string to handle the case where there's just one number
  # get rid of the remaining letters and get the first and last character
  j=$(echo $final$final | sed 's/[^0-9]*//g' | sed 's/\(.\).*\(.\)/\1\2/')
  #echo "....."
  echo $j 
  #echo $j, $t, $final >> numbers.csv
  sum=$(( sum + j ))
  #echo $sum
done < $1

echo $sum
