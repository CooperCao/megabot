## =================================================================================
## Python script to analyse current display
##
## Author A. BUCHET
## =================================================================================

dofusRoot = "/home/aurelien/git/megabot.git/trunk/"
picRoot = dofusRoot + "pictures/"

## =================================================================================
## Packages
## =================================================================================

import time
import numpy as np
import matplotlib.pyplot as plt
#from scipy import signal# using correlation for pattern matching

from PIL import Image
import pyautogui# keyboard, mouse control using python also takes screenshots
import cv2# template matching to find a pattern in an image

##  =================================================================================
##  Fetching Dofus window and screen size
##  =================================================================================

## For now I only got the up/left and down/right corners postitions using
## pyautogui.position()

## defining the game zone coordinates
#x0, y0 = 245, 75
x0, y0 = 241, 76
#x1, y1 = 1175, 614
x1, y1 = 1169, 615

## =================================================================================
## cv2 test
## =================================================================================

# img_rgb = cv2.imread('/home/aurelien/python/dofus/pictures/screen2.png')
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread('/home/aurelien/python/dofus/pictures/test.png',0)
# template_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# w, h = template.shape[::-1]

# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.6
# loc = np.where( res >= threshold)
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

# cv2.imwrite('/home/aurelien/python/dofus/pictures/res.png',img_rgb)

def search(pattern, threshold = 0.6, method = cv2.TM_CCOEFF_NORMED,
           x0 = 241, y0 = 76, x1 = 1169, y1 = 615#for screen reduction in order to reduce elapsed time
):
    """Take the path of a .png and find it in the current screen, returns the positions of the pattern in the screen"""
    ## taking screenshot and converting it to a cv2 compatible grayscale array
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
    ## fetching pattern
    template = cv2.imread(pattern, 0)
    w, h = template.shape[::-1]
    ## matching pattern
    res = cv2.matchTemplate(screen, template, method)
    ## returning the list of points matching the pattern with defined threshold
    return zip(*np.where(res >= threshold)[::-1]) or []

def move(direction):
    """Moves to the next map according to direction ('UP', 'DOWN', 'LEFT' or 'RIGHT')"""
    ## fetching sun positions on the current screen
    loc = search(picRoot + "moving_point.png")
    ## fetching edges in the list of point
    up = down = left = right = loc[0]
    for pt in loc:
        if pt[1] < up[1]:
            up = pt
        if pt[1] > down[1]:
            down = pt
        if pt[0] < left[0]:
            left = pt
        if pt[0] > right[0]:
            right = pt
    if direction == "UP":
        pt = up
    if direction == "DOWN":
        pt = down
    if direction == "LEFT":
        pt = left
    if direction == "RIGHT":
        pt = right
    pyautogui.click(pt)
    return pt

def gather(item, delay = 12):
    """Collects all items on the screen with delay between clicks"""
    ## searching for items
    loc = search(item, threshold = .5)
    ##shuffle to make the bot more realistic and avoid clicking the case under the character
    np.random.shuffle(loc)
    ## browsing fetched points in randow order
    for pt in loc:
        ## clicking on item
        pyautogui.click(pt)
        ## doing the associated action and reaching item
        time.sleep(1)
        action = search(picRoot + "wheat_action.png")
        if len(action):
            pyautogui.click(action[0])
            time.sleep(delay)
    return loc
    
def gather_infinite(item, delay = 12):
    while True:
        gather(item, delay)






    
    
