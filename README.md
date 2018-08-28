# megabot
## Aurélien Buchet - au.buchet@gmail.com

Python gui automation
requires pyautogui and openCV

Pictures are splitten into different folders depending on the resolution of the computer

To do list:
Create a function to click in the middle of a group of points when pattern matches close points (in order to avoid clicks on the edge of a cell)

Available functions:
```python
def search(pattern, threshold = 0.6, method = cv2.TM_CCOEFF_NORMED,
           x0 = 241, y0 = 76, x1 = 1169, y1 = 615#for screen reduction in order to reduce elapsed time
):
    """Take the path of a .png and find it in the current screen, returns the positions of the pattern in the screen"""

def move(direction):
    """Moves to the next map according to direction ('UP', 'DOWN', 'LEFT' or 'RIGHT')"""


```
