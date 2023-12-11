from PIL import Image
from PIL import ImageGrab



def capture(x, y, width, height):
    
    
    # Capture a region of the screen
    box = (x, y + 32, x + width,  y + height)  # Specify the region as (left, top, right, bottom)
    screenshot = ImageGrab.grab(bbox=box)

    # Save the captured region to a file
    screenshot.save("region_screenshot.png")

    


