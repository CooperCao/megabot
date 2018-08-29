## =================================================================================
## Python script to analyse current display
##
## Author A. BUCHET
## =================================================================================

execfile("settings.py")

## =================================================================================
## Main functions
## =================================================================================

def search(pattern, threshold = 0.6, method = cv2.TM_CCOEFF_NORMED,
           bBox = []#for screen reduction in order to reduce elapsed time
):
    """Take the path of a .png and find it in the current screen, returns the positions of the pattern in the screen"""
    ## taking screenshot and converting it to a cv2 compatible grayscale array
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
    ## screen reduction ix bBox is defined
    if bBox:
        x0, y0 = bBox[0]
        x1, y1 = bBox[1]
        screen = screen[y0:y1, x0:x1]
    ## fetching pattern
    template = cv2.imread(pattern, 0)
    w, h = template.shape[::-1]
    ## matching pattern
    res = cv2.matchTemplate(screen, template, method)
    ## returning the list of points matching the pattern with defined threshold
    loc = zip(*np.where(res >= threshold)[::-1])
    if loc:
        return [(pt[0] + w/2, pt[1] + h/2) for pt in loc]
    return []

def searchClick(name, threshold = 0.8, method =  cv2.TM_CCOEFF_NORMED, bBox = []):
    """Search and click the image described by name"""
    loc = search(picRoot + name + ".png", threshold = threshold, method = method, bBox = bBox)
    if len(loc):
        pyautogui.click(loc[0])
        return True
    return False

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

## =================================================================================
## Predicates
## =================================================================================

def inFightp(method = cv2.TM_CCOEFF_NORMED, threshold = .8):
    """Return True if player is fighting, False otherwise"""
    ## taking screenshot
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
    ## checking if 'pret' or 'cac' logo are present on screen
    for pattern in ["pret", "cac"]:
        pattern = picRoot + pattern + ".png"
        template = cv2.imread(pattern, 0)
        res = cv2.matchTemplate(screen, template, method)
        if np.where(res > threshold)[0].any():
            return True
    return False

def fullp(threshold = .8, method = cv2.TM_CCOEFF_NORMED):
    """Return True if player is full, False otherwise"""
    if search(picRoot + "full.png", threshold = threshold, method = method):
        return True
    return False

def levelUpp(threshold = .8, method = cv2.TM_CCOEFF_NORMED):
    """Return True if player is full, False otherwise"""
    return searchClick("up", threshold = threshold, method = method)

def emptyInventoryp(threshold = .9, method = cv2.TM_CCOEFF_NORMED):
    """Return True if current inventory (with selected filter) is empty"""
    if search(picRoot + "empty_inventory.png", threshold = threshold, method = method, bBox = inventoryFirstCellBbox):
        return True
    return False

def emptyBankInventoryp(threshold = .9, method = cv2.TM_CCOEFF_NORMED):
    """Return True if inventory is empty during a bank transaction"""
    if search(picRoot + "empty_inventory.png", threshold = threshold, method = method, bBox = bankInventoryFirstCellBbox):
        return True
    return False
    
## =================================================================================
## Actions
## =================================================================================

def say(text, interval=0.25):
    """Print text in the chat"""
    ## click the chat box
    pyautogui.click(335, 760)
    pyautogui.typewrite("%s\n" % text, interval)
    return text

def eraseChat():
    """Erases current display in the chat (required for some recognition function)"""
    pyautogui.typewrite("gggg")#working only because user is not member of any guild
    #say("%nom% %guilde%")
    #say("%stats% %xp%")
    #say("%vie% %viemax% %viep%")
    #say("%zone% %souszone% %pos%")
      
