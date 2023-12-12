from PIL import Image


def calc():
    
    img = Image.open("region_screenshot.png")
    rgb_values = list(img.getdata())

    for y in range(img.height):
        for x in range(img.width):
            pixel_index = y * img.width + x
            r, g, b = rgb_values[pixel_index]
            
            if r > 140 and g > 140 and b > 140:
                return x, y  
    
    return 0, 0  
    