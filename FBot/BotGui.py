import tkinter as tk
import time
import threading

from BotCapture import capture
from BotCalc import calc
from BotInteract import interact, first_cast

#Create window
window = tk.Tk(screenName="screen")


#Window attributes
window.title("FishBot")
window.geometry("200x226")
window.iconbitmap("Fish_icon.ico")
window.resizable(1,1)

#Make transparent
window.config(bg = '#add123')
window.wm_attributes('-transparentcolor','#add123')


#Button specific attributes
stop_event = threading.Event()


def getWindowPos():
    geometry_info = window.geometry()
    position_info = geometry_info.split('+')[1:]  # Extract Xposition and Yposition
    xPos, yPos = map(int, position_info)
    return xPos, yPos

#Button commands
def captureButtonCommand():
     # Extract Xposition and Yposition
    xPos, yPos = getWindowPos()
    capture(xPos, yPos, window.winfo_width(), window.winfo_height())
    

def startButtonCommand():

    
    startButton.config(state=tk.DISABLED, bg='gray')
    stopButton.config(state=tk.NORMAL, bg="#f0f0f0")
    stop_event.clear()
    xPos, yPos = getWindowPos()
    first_cast(xPos - 1, yPos - 1)

    prev_x, prev_y = 0, 0
    time_prev_cast = 0;
    
    while not stop_event.is_set():
        
        captureButtonCommand()
        xPos, yPos = getWindowPos()
        x, y = calc()
        
        if (x == 0 and y == 0 and prev_x != 0 and prev_y != 0) or time_prev_cast > 180: 
            interact(prev_x + xPos -5, prev_y + yPos + 35)
            time_prev_cast = 0

        prev_x = x
        prev_y = y
        time_prev_cast += 1
        time.sleep(0.10)
        

def stopButtonCommand():

    startButton.config(state=tk.NORMAL, bg="#f0f0f0")
    stopButton.config(state=tk.DISABLED, bg='gray')
    stop_event.set()
    
    



startButton = tk.Button(window, text="Start", command=lambda: threading.Thread(target=startButtonCommand).start())
startButton.pack(side=tk.LEFT, anchor=tk.SW)

stopButton =tk.Button(window, text="Stop", command=stopButtonCommand, state=tk.DISABLED, bg="gray")
stopButton.pack(side=tk.LEFT, anchor=tk.SW)



#Mainloop
window.mainloop()  