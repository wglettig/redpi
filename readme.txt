This Raspberry Pi provides a RESTful API to access the GPIO PWM.
The RESTful API can be used like this:

curl -X PUT -d val=100 redpi:5000

To do this the script ~/AutoStart/server.py is called as a cron job
(sudo crontab -e)
(@reboot python /home/pi/AutoStart/server.py &)
