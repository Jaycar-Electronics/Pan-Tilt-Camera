#!/bin/bash

sudo /etc/init.d/servoblaster.sh stop
sudo update-rc.d servoblaster.sh remove
sudo rm -f /etc/init.d/servoblaster.sh
sudo rm -f /usr/local/sbin/servod

echo " -- Done -- "
