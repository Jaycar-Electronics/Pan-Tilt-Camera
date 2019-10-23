
# set up mirrors for australian servers (quicker)
./mirrors.sh

# do a quick update
sudo apt-get update
sudo apt-get upgrade -y

ROOTDIR=$(pwd)

# firstly install the camera interface

wget https://github.com/silvanmelchior/RPi_Cam_Web_Interface/archive/master.zip
unzip master.zip
mv RPi_Cam_Web_Interface-master web-interface
rm master.zip
cp rpi-camera.cfg -v web-interface/config.txt

cd web-interface

./install.sh

# then activate the pan-tilt functions
cd $ROOTDIR

source rpi-camera.cfg
#enable pantilt
sudo mv /var/www/$rpicamdir/pipan_off /var/www/$rpicamdir/pipan_on
sudo mknod /var/www/$rpicamdir/FIFO_pipan p 
sudo chmod 666 /var/www/$rpicamdir/FIFO_pipan 

PIPAN_FIFO_LOCATION=/var/www/$rpicamdir/FIFO_pipan
export PIPAN_FIFO_LOCATION


#install pipan
sudo mkdir -p /usr/local/lib/python3.7/dist-packages
sudo mv pantilt/pi-pan/pipan.py /usr/local/lib/python3.7/dist-packages

# now install pan tilt
cd $ROOTDIR/pantilt
./install.sh

sudo sed -i "$ i export PIPAN_FIFO_LOCATION=/var/www/$rpicamdir/FIFO_pipan" /etc/rc.local
sudo sed -i '$ i #run pantilt fifo' /etc/rc.local
sudo sed -i '$ i ptpiper.py &' /etc/rc.local

#cd $ROOTDIR
ip=$(hostname -I) || true
echo "Webserver running on http://$ip";
sudo reboot #just to be safe