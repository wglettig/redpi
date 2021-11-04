This Raspberry Pi provides a RESTful API to access the GPIO PWM.
The RESTful API can be used like this:

curl -X PUT -d val=100 redpi:5000

To do this the script ~/AutoStart/server.py is called as a cron job
(sudo crontab -e)
(@reboot python /home/pi/AutoStart/server.py &)

Install with
git clone https://github.com/wglettig/redpi

Install vim
sudo apt install vim

Make sure PSI Timeserver is active:
sudo apt install ntp
Add the PSI time server in the file /etc/ntp.conf : 
server pstime1.psi.ch burst iburst
server pstime2.psi.ch burst iburst
server pstime3.psi.ch burst iburst
Restart NTP service:
sudo service ntp restart
Test with:
ntpq -p
or
date

Make sure Python 3 is active:
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2
sudo update-alternatives --config python
python --version

Install flask_restful
pip3 install flask-restful
