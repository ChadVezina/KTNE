import cv2, pyautogui, time, numpy as np
from PIL import ImageGrab

pyautogui.FAILSAFE = False
#YELLOW_LOWER = np.array([187, 150, 0], dtype="uint8")
YELLOW_LOWER = np.array([255, 204, 0], dtype="uint8")
YELLOW_UPPER = np.array([255, 204, 0], dtype="uint8")
#left = "left"
#right = "right"
#down = "down"
left = "a"
right = "d"
down = "s"


def back_flip():  # performs a back flip
    print("down+space")
    return
    pyautogui.press(down)
    pyautogui.press("space")
    print("back-flipping")


def cart_slam():  # performs a cart slam
    print("space+down")
    return
    pyautogui.press("space")
    pyautogui.press(down)
    print("cart-slamming")


def drift(dir):  # performs a drift turn
    print("drifting start: " + dir)
    time.sleep(1)
    print("drifting end: " + dir)
    return
    pyautogui.keyDown(down)
    pyautogui.keyDown(dir)
    print("drifting " + dir)
    time.sleep(1)
    pyautogui.keyUp(down)
    pyautogui.keyUp(dir)


def debug(grab):  # method to view what the program is seeing for bug testing
    cv2.imshow("Frame", grab)                                          # raw capture
    cv2.imshow("Mask", cv2.inRange(grab, YELLOW_LOWER, YELLOW_UPPER))  # yellow masked capture (what it's detecting)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_sign(dir, x1, y1, x2, y2):
    frame_grab = ImageGrab.grab(bbox=(x1, y1, x2, y2))  # capture information on screen in XY region
    frame = np.array(frame_grab)                        # convert information to image
    #debug(frame)
    if 255 in cv2.inRange(frame, YELLOW_LOWER, YELLOW_UPPER):  # detect for yellow in captured image
        cart_slam()     # get some extra points and allow full 100 for next back flip
        time.sleep(.4)  # wait .4 seconds
        drift(dir)      # perform a drift in the necessary direction
        back_flip()     # perform a back flip after the drift/turn


def get_all():
    left_x1 = 710
    left_y1 = 350

    left_x2 = 1115
    left_y2 = 1498

    right_x1 = 2720
    right_y1 = 350

    right_x2 = 3128
    right_y2 = 1498

    return left_x1, left_y1, left_x2, left_y2, right_x1, right_y1, right_x2, right_y2


def get_all2():
    left_x1 = 1356
    left_y1 = 642

    left_x2 = 1544
    left_y2 = 1185

    right_x1 = 2294
    right_y1 = 642

    right_x2 = 2488
    right_y2 = 1185

    return left_x1, left_y1, left_x2, left_y2, right_x1, right_y1, right_x2, right_y2


def get_all3():
    left_x1 = 241
    left_y1 = 648

    left_x2 = 1449
    left_y2 = 1243

    right_x1 = 2391
    right_y1 = 648

    right_x2 = 3608
    right_y2 = 1243

    return left_x1, left_y1, left_x2, left_y2, right_x1, right_y1, right_x2, right_y2


all = get_all3()
while True:
    #time.sleep(1)
    #x = pyautogui.position()  # get the current mouse position
    #print(x)  # print the current mouse position
    detect_sign(right, all[0], all[1], all[2], all[3])
    detect_sign(left, all[4], all[5], all[6], all[7])
    #detect_sign(right, 400, 640, 1000, 955)
    #detect_sign(left, 1500, 640, 2000, 955)