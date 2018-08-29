## =================================================================================
## Python script to automate jobs
## =================================================================================

## =================================================================================
## Loading required files
## =================================================================================

execfile("settings.py")
execfile("analyse_screen.py")

## =================================================================================
## Actions
## =================================================================================

def gather(item, delay = 10):
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
        time.sleep(.5)
        action = search(actionPicture, threshold = .9)
        ## if associated action appeared click it it and wait til next action is available
        if len(action):
            pyautogui.click(action[0])
            ## wait for action + random delay to act more natural
            time.sleep(delay + random.random() * 2)
        if inFightp():
            mail("Enterred Fight")
            break
        if fullp():
            break
        if levelUpp():
            mail("Job Levelled Up")
    return loc
      
def goToBank():
    """Uses a potion to go to Bonta and uses zaapi to enter the bank then empty inventory in the bank"""
    ## open inventory
    searchClick("inventory")
    time.sleep(1)
    ## goto misc tab 
    searchClick("misc")
    time.sleep(1)
    ## expand search bar
    searchClick("expandArrow")
    time.sleep(1)
    ## goto potion tab
    searchClick("potion")
    time.sleep(1)
    ## use bonta potion
    searchClick("bonta")
    pyautogui.click()#doubleclick to use potion
    time.sleep(3)
    ## use zaapi
    searchClick("zaapi", threshold = .6)
    searchClick("zaapi_action", threshold = .9)
    time.sleep(1)
    searchClick("zaapi_divers", threshold = .9)
    time.sleep(1)
    searchClick("zaapi_banque", threshold = .9)
    time.sleep(1)
    ## enter bank
    pyautogui.click(838, 318)
    time.sleep(3)
    searchClick("banker")
    time.sleep(1)
    searchClick("banker_action")
    time.sleep(1)
    searchClick("banker_action2")
    time.sleep(1)
    ## go to resources tab
    searchClick("resources")#first time for left window
    searchClick("resources")#second time for right window (left window is not recognized anymore)
    time.sleep(1)
    ## move to first item in inventory
    while not emptyInventoryp():
        pyautogui.moveTo(949, 292)
        pyautogui.dragTo(288, 292, duration = .5)
        time.sleep(.2)
        searchClick("max")
        time.sleep(.2)
        searchClick("ok", threshold = .95)
    time.sleep(.2)
    return searchClick("close")

def gather_infinite(item, delay = 12):
    while not fullp() and not inFightp():
        gather(item, delay)
    if fullp():
      mail("Inventory is full")
      ## display messages to remove "inventaire plein
      ## votre récolte est perdue" from the screen
      eraseChat()
      ## need to go to bank to empty inventory
      goToBank()
