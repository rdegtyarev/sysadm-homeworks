#!/usr/bin/env bash
array_int=(0 1 2 3 4)
array_hosts=("http://192.168.0.1:80" "http://173.194.222.113:80" "http://87.250.250.242:80")
for i in ${array_int[@]}
do
for m in ${array_hosts[@]}
do
curl $m
if (($?==0))
then
echo Ok
echo $(date) $m - Ок >> test.log
else
echo $(date) $m - Error >> test.log
fi
done
done