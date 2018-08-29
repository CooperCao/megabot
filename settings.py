## =================================================================================
## Packages
## =================================================================================

import os# to use mail in sh
import time
import random

import numpy as np
import matplotlib.pyplot as plt
#from scipy import signal# using correlation for pattern matching

from PIL import Image
import pyautogui# keyboard, mouse control using python also takes screenshots
import cv2# template matching to find a pattern in an image

## =================================================================================
## Variables definition
## =================================================================================

dofusRoot = "/home/aurelien/git/megabot.git/trunk/"
picRoot = dofusRoot + "pictures/"
player = "au.buchet@gmail.com"

##  =================================================================================
##  Fetching Dofus window and screen size
##  =================================================================================

## For now I only got the up/left and down/right corners postitions using
## pyautogui.position()

mapBbox = (241, 76), (1169, 615)
screenBbox = (), ()
bankInventoryFirstCellBbox = (933, 277), (966, 308)

## =================================================================================
## Sending mail to user
## =================================================================================

def mail(subject, text = "", adress = player, attachments = []):
  os.system('mail -s "%s" %s < %smail.txt' % (subject, adress, dofusRoot))

