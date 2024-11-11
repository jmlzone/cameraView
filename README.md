# cameraView
Python view for rtsp cameras 8 cameras in a 3x3 grid, simple python tk with vlc player
Tested on raspberryPi 3 and 5.  May work on other linux machines.  

setup:
 update the python for your ip address/url/username and password.  This is setup for a cobra DVR.  Other dvr's may use different urls

sudo apt install -y python3-vlc

 ./cameraView.py

 The python is simple enough you should be able to update it yourself.  I'm sure I will contiue to improve it.  It is a bit sluggish runing 8 vlc viewers on a pi.
 
