from PIL import ImageGrab



def capture(x, y, width, height):
    
    
    # Capture a region of the screen
    box = (x, y + 32, x + width,  y + height)  
    screenshot = ImageGrab.grab(bbox=box)

    screenshot.save("region_screenshot.png")

    


