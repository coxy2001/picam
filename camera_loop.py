from picamera import PiCamera
from time import sleep
import subprocess

wait_time = 60 * 3
#wait_time = 3
cam = PiCamera()

while True:
    try:
        # Capture photo
        cam.start_preview()
        sleep(3)
        cam.capture("/var/www/html/photo.jpg")
        cam.stop_preview()
    except:
        print("Photo Capture ERROR!!")
        subprocess.call(['sh', '/home/pi/reboot.sh'])

    # Update cloudflair ddns
    subprocess.call(['sh', '/home/pi/cloudflair-ddns-update.sh'])
    # Wait set time
    sleep(wait_time)
