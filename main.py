import os
from PIL import Image
print("Ascii Converter")

directory = input("Enter the picture's directory: ")

os.chdir(directory.rsplit('\\', 1)[0])  # Folder we are currently in Example: C:\Users\Eric\Desktop\thug.png
im = Image.open(directory.split('\\')[-1])  # Image stored in that folder

im.thumbnail((64, 64))  # rescale image to 64x64 pixels
width, height = im.size  # declaring width and height
im = im.rotate(270).transpose(Image.FLIP_LEFT_RIGHT)  # rotate and flip image so printing comes in right orientation
print(str(width) + " x " + str(height))


pixel_matrix = []  # empty array that will store RGB values at x,y coordinates
pixel = im.convert("RGB")  # Convert Image into Raw RGB values

for x in range(width):
    for y in range(height):
        pixel_matrix.append([pixel.getpixel((x, y))])  # getpixel() returns RGB value at x,y

ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"  # ascii characters for art!

bright_list = []  # empty array that will store Brightness levels at x,y coordinates
for x in range(len(pixel_matrix)):  # convert into brightness
    for y in range(len(pixel_matrix[x])):
        data = pixel_matrix[x][y]  # declaring RGB value from pixel_matrix
        brightness = (data[0] + data[1] + data[2]) / 3  # Convert RGB into Brightness using Average: (R + G + B) / 3
        brightness = round(brightness)
        bright_list.append(brightness)


def split(word):  # function to split words into individual characters
    return [char for char in word]


# Convert Brightness into ASCII characters
ascii_list = split(ascii_chars)  # converting ascii_chars from "XYZ" to ["X","Y","Z"]
list_word = []
for i in range(len(bright_list)):
    num = round(bright_list[i] / 4)  # 255 / 4 = 64 close number to len(ascii_chars) = 68
    list_word.append(ascii_list[num])  # the text is the index of num in ascii_list
    if i % width == 0:  # if i / width = 1 then print a new line to seperate the picture
        list_word.append('\n')
print(''.join(list_word))  # split new lines at the width of the image
