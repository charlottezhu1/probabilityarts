# import tkinter as tk
import random
import numpy as np
from PIL import Image
from PIL import ImageDraw

# markov_dict = {}

def createImage(n, baseImage, distribution):
    img = Image.open('/Users/xuyangzhu/Desktop/storefront/utils/assets/sunsets/{}.jpg'.format(baseImage))
    
    
    # img = Image.open('/Users/xuyangzhu/Desktop/Project/Probability_Art/assets/leaves/leaves6.jpg')
    img = img.convert("RGB")
    n = int(n)
    markov_dict = build_markov(img)
    image = random_walk(markov_dict, n, distribution)
    print("done drawing, returning image!")
    # image = create_image(markov_dict)
    # show_image(image, n, distribution)
    return image


## Loop over pixels in the reference image, create a markov dict ##
def build_markov(img):
    markov_dict = {}
    print("it's building markov!")
    
    pixels = img.load()
    # markov_dict = {}
    width, height = img.size
   
    for x in range(width):
        for y in range(height):
            
            current = pixels[x, y]
            
            if current not in markov_dict:
                markov_dict[current] = []
            
            if x > 0:
                left = pixels[x - 1, y]
                markov_dict[current].append(left)
            if x < width - 1:
                right = pixels[x + 1, y]
                markov_dict[current].append(right)
            if y > 0:
                up = pixels[x, y - 1]
                markov_dict[current].append(up)
            if y < height - 1:
                down = pixels[x, y + 1]
                markov_dict[current].append(down)  
    
    print("markov done!")
    return markov_dict


## Color pixels in ordered ways - this create strips! ##
def create_image(markov_dict):
    image = Image.new("RGB", (600, 600), "white")
    current = random.choice(list(markov_dict.keys()))
    
    for x in range(600):
        for y in range(600):
            image.putpixel((x, y), current)
            next = random.choice(list(markov_dict[current]))
            current = next
            
    return image


## Random Walk ##
def random_walk(markov_dict, n, sampling_method):
    print("it's running random walk!")
    width, height = 600, 600
    image = Image.new("RGB", (width, height), "white")
    
    # create a set of uncolored pixels
    uncolored_set = set()
    for x in range(width):
        for y in range(height):
            uncolored_set.add((x, y))
            
    # initialize the pixel set
    # Random sampling!
    if sampling_method == "Uniform Distribution": pixel_set = random_sampling(n, width, height, markov_dict)
    
    # Pareto sampling!
    if sampling_method == "Pareto Distribution": pixel_set = pareto_sampling(n, width, height, markov_dict)
    
    # Normal sampling!   
    if sampling_method == "Normal Distribution": pixel_set = normal_sampling(n, width, height, markov_dict)
    
    print("coloring the image! just one sec~!")

    draw_starting_points(image, pixel_set)
    output = iterative_draw_random(image, markov_dict, pixel_set, uncolored_set)
    return output


## Uniform Distribution ##
def random_sampling(n, width, height, markov_dict):
    print("using Random Sampling for starting points!")
    pixel_set = set()
    for i in range(n):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        
        current_color = random.choice(list(markov_dict.keys()))
        current_elem = ((x, y), current_color)
        pixel_set.add(current_elem)
    return pixel_set


## Pareto Distribution ##
def pareto_sampling(n, width, height, markov_dict):
    print("using Pareto Sampling for starting points!")
    pixel_set = set()
    while len(pixel_set) < n:
        x = int(np.random.pareto(1.6))
        y = int(np.random.pareto(1.6))
        # y = random.randint(0, height - 1)
        # y = int(np.random.normal(300, 200))
        
        if 0 < x < width and 0 < y < height:
            current_color = random.choice(list(markov_dict.keys()))
            current_elem = ((x, y), current_color)
            pixel_set.add(current_elem)
            # diagnal_elem = ((width - x, height - y), current_color)
            # pixel_set.add(diagnal_elem)
    return pixel_set
    
    
## Normal Distribution ##   
def normal_sampling(n, width, height, markov_dict):
    print("using Normal Sampling for starting points!")
    mean_x = width/2
    mean_y = height/2
    sdv_x = width/2
    sdv_y = height/2
    
    pixel_set = set()
    while len(pixel_set) < n:
        x = int(np.random.normal(mean_x, sdv_x))
        y = int(np.random.normal(mean_y, sdv_y))
        
        if 0 < x < width and 0 < y < height:
            current_color = random.choice(list(markov_dict.keys()))
            current_elem = ((x, y), current_color)
            pixel_set.add(current_elem)
    return pixel_set


## Random Walk Draw: ITERATIVE CODE ##
def iterative_draw_random(image, markov_dict, pixel_set, uncolored_set):
    width, height = image.size
    
    iteration = 0
    while len(pixel_set) != 0:
        if iteration == 90000:
            image.save('./storefront/static/createdArt/step1.jpg')
        if iteration == 180000:
            image.save('./storefront/static/createdArt/step2.jpg')
        if iteration == 270000:
            image.save('./storefront/static/createdArt/step3.jpg')
        
        iteration += 1
        elem = pixel_set.pop()
        
        # color the current pixel
        x = elem[0][0]
        y = elem[0][1]
        current = elem[1]
        image.putpixel((x, y), current)
        
        # add all the adjacent pixels into the list
        colors = markov_dict[current]
        if x > 0:
            left = (x - 1, y)
            if left in uncolored_set:
                # check whether a pixel is already colored
                pixel_set.add((left, random.choice(colors))) 
                uncolored_set.discard(left)
                
        if x < width - 1:
            right = (x + 1, y)
            if right in uncolored_set:
                pixel_set.add((right, random.choice(colors)))
                uncolored_set.discard(right)
                
        if y > 0:
            up = (x, y - 1)
            if up in uncolored_set:
                pixel_set.add((up, random.choice(colors)))
                uncolored_set.discard(up)
                
        if y < height - 1:
            down = (x, y + 1)
            if down in uncolored_set:
                pixel_set.add((down, random.choice(colors)))
                uncolored_set.discard(down)
                
    print("The while loop ran for:", iteration, "iterations!")
    return image  


def draw_starting_points(image, pixel_set):
    print("drawing starting points on canvas!")
    draw = ImageDraw.Draw(image)
    for elem in pixel_set:
        x = elem[0][0]
        y = elem[0][1]
        bounding_box = (x, y, x + 2, y + 2)
        draw.ellipse(bounding_box, fill="black")
    image.save('./storefront/static/createdArt/startingpoints.jpg')
    print("saved the image of the starting points!")


## DISPLAY IMAGE ##
# def show_image(img, n, sample_index):
#     root = tk.Tk()
#     # sampling_ways = ["random", "pareto", "normal"]
#     # sample = sampling_ways[sample_index]
#     root.title("Your Art - created with " + str(n) + " starting points from " +  sample_index + " ~!")
    
#     tk_image = ImageTk.PhotoImage(img)
    
#     label = tk.Label(root, image=tk_image)
#     label.pack()
    
#     root.mainloop()
                       
if __name__ == '__main__':
    createImage(10, "sunset1","Uniform Distribution")                        