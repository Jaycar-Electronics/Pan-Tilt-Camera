#!/bin/bash

if [ -e  servo/servod ]  && [ -e servo/ptneutral.py ] && [ -e servo/ptpiper.py ]
then

    sudo cp servo/servod /usr/local/sbin
    sudo cp servo/ptneutral.py /usr/local/sbin
    sudo cp servo/ptpiper.py /usr/local/sbin
else
    echo "servo/servod  or other files not not found"
    exit 1
fi

if [ -e  servo/servoblaster.sh ]
then
    sudo cp servo/servoblaster.sh /etc/init.d
else
    echo "servo/servoblaster.sh not found"
    exit 1
fi

sudo update-rc.d servoblaster.sh defaults 92 08
sudo /etc/init.d/servoblaster.sh start > /dev/null

echo " -- Done -- "
