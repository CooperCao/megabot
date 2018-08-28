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


    
    
