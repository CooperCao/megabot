## =================================================================================
## Python script to automate jobs
## =================================================================================

## =================================================================================
## Loading required files
## =================================================================================

execfile("settings.py")
execfile("analyse_screen.py")

def gather(item, delay = 12):
    """Collects all items on the screen with delay between clicks"""
    ## fetching path of item and associated actions (screenshots)
    picture = picRoot + item + ".png"
    actionPicture = picRoot + item + "_action.png"
    ## searching for items
    loc = search(picture, threshold = .5)
    ## shuffling to make the bot more realistic and
    ## avoid clicking the case under the character
    np.random.shuffle(loc)
    ## browsing fetched points
    for pt in loc:
        ## clicking on item
        pyautogui.click(pt)
        ## doing the associated action and reaching item
        time.sleep(1)
        action = search(actionPicture, threshold = .8)
        if len(action):
            pyautogui.click(action[0])
            time.sleep(delay)
    return loc
    
def gather_infinite(item, delay = 12):
    while True:
        gather(item, delay)



