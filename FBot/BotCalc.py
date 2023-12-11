from PIL import Image
import matplotlib.pyplot as plt



squares = [[] for _ in range(16)]

def calc():
    
    img = Image.open("region_screenshot.png")
    rgb_values = list(img.getdata())

    for y in range(img.height):
        for x in range(img.width):
            pixel_index = y * img.width + x
            r, g, b = rgb_values[pixel_index]
            
            if r > 140 and g > 140 and b > 140:
                return x, y  # Return the first coordinates meeting the condition
    
    return 0, 0  # Return default coordinates if no coordinates meet the condition
            
            
            #Append the sum of RGB values to the corresponding square's list
            #square_index = (y // 50) * 4 + (x // 50)
            #squares[square_index].append(sum_rgb)

    