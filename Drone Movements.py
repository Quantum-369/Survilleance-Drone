from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

#drone.takeoff()
# send remote control speeds
#drone.send_rc_control(0,50,0,0) # move forwardvelocity 50cm/sec
#sleep(2)
#drone.send_rc_control(0,50,0,0) # backwardvelocity -50
#sleep(2)
#drone.send_rc_control(0,0,0,0) # helicopter landing
#drone.land()


