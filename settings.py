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
inventoryFirstCellBbox = (976, 268), (999, 285)#(968, 250), (1015, 300)
bankInventoryFirstCellBbox = (933, 277), (966, 308)

## =================================================================================
## Sending mail to user
## =================================================================================

def mail(subject, text = "", adress = player, attachments = []):
  command = 'mail -s "%s" %s < %smail.txt' % (subject, adress, dofusRoot) 
  os.system(command)
  return command
  

## =================================================================================
## Middle of a bounding box
## =================================================================================

def bBoxMiddle(bBox):
  """return the point in the middle of a bounding box"""
  x0, y0 = bBox[0]
  x1, y1 = bBox[1]
  return (x0 + x1) / 2 , (y0 + y1) /2 

