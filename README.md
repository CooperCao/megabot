# megabot
## Aurélien Buchet - au.buchet@gmail.com

Python gui automation
requires pyautogui and openCV

TO DO LIST:
Creates different folder in pictures if image recognition is resolution/screen dependant
Creates fuctions to give current position, current kamas amount on character (in bank), level, jobs levels, pods and max pods
Creates function to go to bank/fields/astrub without using potion or zaap
functions to locate character or opponents in combat, to move, to attack...

Available functions:
```python
def search(pattern, threshold = 0.6, method = cv2.TM_CCOEFF_NORMED,
           x0 = 241, y0 = 76, x1 = 1169, y1 = 615#for screen reduction in order to reduce elapsed time
):
    """Take the path of a .png and find it in the current screen, returns the positions of the pattern in the screen"""

def move(direction):
    """Moves to the next map according to direction ('UP', 'DOWN', 'LEFT' or 'RIGHT')"""


```

UBUNTU 18.04 Setup:

game installation:

openCV installation:

tesseract installation:
```shell
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev
sudo pip install pytesseract
```
