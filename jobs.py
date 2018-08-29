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

def gather(items, action, delay = 10, threshold = .5):
    """Collects all items on the screen with delay between clicks"""
    ## converting items into a list if it is only one item
    if items is str:
        items = [items]
    loc = []
    for item in items:
        ## searching for item
        loc += search(item, threshold = threshold)
        ## shuffling to make the bot more realistic and
        ## avoid clicking the case under the character
    np.random.shuffle(loc)
    ## browsing fetched points
    for pt in loc:
        ## clicking on item
        pyautogui.click(pt)
        ## doing the associated action and reaching item
        time.sleep(.5)
        act = search(action, threshold = .9)
        ## if associated action appeared click it it and wait til next action is available
        if len(act):
            pyautogui.click(act[0])
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
    time.sleep(3)#waiting for zone name to disappear
    ## use zaapi
    searchClick("zaapi", threshold = .6)
    time.sleep(.2)
    searchClick("zaapi_action", threshold = .8)
    time.sleep(1)
    #searchClick("zaapi_divers")
    pyautogui.click(555, 169)
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
    ## move to first item in inventory and emptyn the inventory
    while not emptyBankInventoryp():
        pyautogui.moveTo(bBoxMiddle(bankInventoryFirstCellBbox))
        pyautogui.dragTo(288, 292, duration = .5)
        time.sleep(.2)
        searchClick("max")
        time.sleep(.2)
        searchClick("ok", threshold = .95)
    time.sleep(.2)
    return searchClick("close")

def goToAstrub(save = False):
    """Comes back to astrub's zaap using a potion and a zaap if necessary"""
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
    ## use potion
    searchClick("rappel")
    pyautogui.click()#doubleclick to use potion
    time.sleep(3)#waiting for zone name to disappear

    ## need to check if astrub is the saved postion
    if True:
        ## uses zaap
        searchClick("zaap")
        time.sleep(1)
        searchClick("zaap_action", threshold = .8)
        time.sleep(1)
        searchClick("zaap_astrub",)


def goToAstrubFields():
    """Go to astrub the go up in to astrub fields"""
    goToAstrub()
    
    
def emptyBags():
    """Empty resources bag in inventory"""
    ## open inventory
    searchClick("inventory")
    time.sleep(1)
    ## goto misc tab 
    searchClick("misc")
    time.sleep(1)
    ## expand search bar
    searchClick("expandArrow")
    time.sleep(1)
    ## goto resources bags tab
    if searchClick("resources_bag"):
        time.sleep(1)
        while not emptyInventoryp():
            pyautogui.moveTo(bBoxMiddle(inventoryFirstCellBbox))
            pyautogui.click()
            pyautogui.click()
            time.sleep(.4)
    return searchClick("close")

def farm(items = ["wheat", "oat", "barley"], delay = 10, threshold = .5):
    items = [picRoot + "farmer/" + item + ".png" for item in items]
    action = picRoot + "farmer/action.png"
    while not fullp() and not inFightp():
        gather(items, action, delay)
    if fullp():
      mail("Inventory is full")
      ## display messages to remove "inventaire plein
      ## votre récolte est perdue" from the screen
      eraseChat()
      ## empty resources bags
      emptyBags()
      ## go to bank to empty inventory
      goToBank()
