import numpy as np
import functools
import sys
import cv2

def checkImageFormat(img):
    if img[-4:] != '.png':
        print("Please select a image that is a png, repeat!")
        sys.exit()

def embedding_info(picname, savename, text):
    try:        
        im = cv2.imread(picname)
    except:
        print("Cannot obtain image, please check file name")
        sys.exit()

    count = 0
    embed = []
    text += '#%#'
    rows, columns, colors = im.shape

    for c in text:
        bin_sign = (bin(ord(c))[2:]).zfill(16)
        for i in range(16):
            embed.append(int(bin_sign[i]))

    print(embed)
    for row in range(rows):
        for col in range(columns):
            for color in range(colors):
                if count < len(embed):
                    #It divides it by 2 and rounds down to the nearest even number using the floor division operator "// 2 * 2". 
                    #This is done to clear the LSB of the color component so that it can be replaced with the next bit of the message.
                    im[row][col][color] = im[row][col][color] // 2 * 2 + embed[count] 
                    count += 1

    cv2.imwrite(savename, im)

def extract_info(picname):
    try:
        im = cv2.imread(picname)
    except:
        print("Cannot obtain image, please check file name")
        sys.exit()

    rows, columns, colors = im.shape
    text = ""
    count = 0
    extract = np.array([], dtype=int) #empty array to store the LSB of certain pixels

    for row in range(rows):
        for col in range(columns):
            for color in range(colors):
                extract = np.append(extract, im[row][col][color] % 2)
                count += 1
                if count % 16 == 0: #A full character has been extracted
                    bcode = functools.reduce(lambda x, y: str(x) + str(y), extract) #Convert the bits into a binary string
                    cur_char = chr(int(bcode, 2)) #Convert the number for the ASCII value
                    text += cur_char
                    if cur_char == '#' and text[-3:] == '#%#':
                        return text[:-3]
                    extract = np.array([], dtype=int)

print("Digital Watermarking - Example 1")
option=1
while option != 0:
    option = input("\t1 - Watermark Embedding\n\t2 - Watermark Extracting\n\tOther - exit\n\t>> ")
    if option == '1':
        imagePath = input("Path of the image to be embeded: ")
        #DEBUG
        imagePath = "Original Images\\dog.png"
        checkImageFormat(imagePath)
        watermark = input("Text for watermark: ")
        #DEBUG
        watermark="Here goes the watermark"
        embedding_info(imagePath, 'Watermarked Images\\dog_ex1.png', watermark)
    elif option == '2':
        imagePath = input("Path for the image to extract: ")
        #DEBUG
        imagePath = "Watermarked Images\\dog_ex1.png"
        checkImageFormat(imagePath)
        text = extract_info(imagePath)
        print("Extracted Information:", text)
    else:
        sys.exit()