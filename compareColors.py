from PIL import Image


def get_main_color(file):
    img = Image.open(file)
    colors = img.getcolors(256)  # put a higher value if there are many colors in your image
    max_occurrence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurrence:
                (max_occurrence, most_present) = c
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")


print(get_main_color("/Users/marcobarreirinhas/Desktop/mineStone.jpg"))

img = Image.open("/Users/marcobarreirinhas/Desktop/mineStone.jpg")
colors = img.getcolors(256)
for c in colors:
    print(c)