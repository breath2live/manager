
#!/bin/bash
for (( ; ; ))
do
clear
echo "Starting:" $1
python3 $1
echo "Done!"
date

sleep $2

done
