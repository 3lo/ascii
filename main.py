import os
from PIL import Image
print("Ascii Converter")

os.chdir('C:\\Users\\Eric\\Desktop')
im = Image.open("pineapple.jpg")
width, height = im.size
print(str(width) + " x " + str(height))

pixel_matrix = []
pixel = im.convert("RGB")

for x in range(width):
    for y in range(height):
        pixel_matrix.append([pixel.getpixel((x, y))])

ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
# convert into brightness
bright_list = []
for x in range(len(pixel_matrix)):
    for y in range(len(pixel_matrix[x])):
        data = pixel_matrix[x][y]
        brightness = (data[0] + data[1] + data[2]) / 3  # Convert RGB into Brightness using Average: (R + G + B) / 3
        brightness = round(brightness)
        bright_list.append(brightness)  # Convert Brightness into ASCII characters


def split(word):
    return [char for char in word]


ascii_list = split(ascii_chars)
list_word = []
for i in range(len(bright_list)):
    num = round(bright_list[i] / 4)
    list_word.append(ascii_list[num])
    if i % height == 0:
        list_word.append('\n')
print(''.join(list_word))  # split new lines at the width of the image

# A brightness of 0 should map to a delicate backtick (`), and a brightness of 255 should map to big stocky dollar sign ($)
'''
fmt.Print(string("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"[uint32(brightness)/4]))
'''
