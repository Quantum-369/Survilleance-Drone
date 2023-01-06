import pygame
from djitellopy import tello
import time
import Keymodule as km  # importing the keymodule here
import cv2

km.init()  # initializing the pygame window
drone = tello.Tello()
drone.connect()
print(drone.get_battery())
drone.streamon()

global img

def getkeyinp():
    lr, fb, ud, yaw = 0, 0, 0, 0
    speed = 40
    if km.getKey("LEFT"):
        lr = -speed
    elif km.getKey("RIGHT"):
        lr = speed
    if km.getKey("UP"):
        fb = speed
    elif km.getKey("DOWN"):
        fb = -speed
    if km.getKey("u"):
        ud = speed
    elif km.getKey("d"):
        ud = -speed
    if km.getKey("c"):
        yaw = -speed
    elif km.getKey("a"):
        yaw = speed
    if km.getKey("t"):
        drone.takeoff()
    elif km.getKey("l"):
        drone.land()
        time.sleep(3)
    if km.getKey("x"):
        pygame.quit()
    if km.getKey("p"): # press "p" to take and save a picture
        cv2.imwrite(f'DRONEIMAGES/{time.time()}.jpg',img)
        time.sleep(0.2) # avoids multiple image savings

    return [lr, fb, ud, yaw]


while True:
    values = getkeyinp()
    drone.send_rc_control(values[0], values[1], values[2], values[3])
    # capture the frame
    img = drone.get_frame_read().frame
    # to process the image faster we need to resize the image with help of Opencv

    img = cv2.resize(img, (360, 240))

    cv2.imshow("DRONE IMAGE", img)
    cv2.waitKey(1)
    if ord('v') == cv2.waitKey(1) & 0xFF:  # escape key waiting
        break
    time.sleep(0.05)
