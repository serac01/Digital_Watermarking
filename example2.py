import cv2 as cv
import numpy
import hashlib
import sys

ColRange = 16
RowRange = 16

def hash(ID):
    hash_method = hashlib.sha256()
    hash_method.update(ID.encode('utf-8'))
    binary = []
    temp = []
    result = []
    str = hash_method.hexdigest()

    for i in str:
        if i >= '0' and i <= '9':
            b = ord(i) - 48
        else:
            b = ord(i) - 55
        while (len(temp) < 4):
            temp.append(b % 2)
            b //= 2
        while (len(temp) > 0):
            binary.append(temp.pop())

    result.append(str)
    result.append(binary)
    return result

def arnold(picture):
    An = numpy.zeros([height, width, 3])
    n = 2
    a = 3
    b = 5
    N = min(height, width)
    for i in range(1, n):
        for y in range(N):
            for x in range(N):
                xx = (x + b * y) % N
                yy = (a * x + (a * b + 1) * y) % N
                An[yy][xx] = picture[y][x]
    if height > width:
        for y in range(N, height):
            for x in range(N):
                An[y][x] = picture[y][x]
    elif height < width:
        for y in range(N):
            for x in range(N, width):
                An[y][x] = picture[y][x]

    return An

def recover(picture):
    An = numpy.zeros([height, width, 3])
    n = 2
    a = 3
    b = 5
    N = min(height, width)
    for i in range(1, n):
        for y in range(N):
            for x in range(N):
                xx = ((a * b + 1) * x - b * y) % N
                yy = (a * x * -1 + y) % N
                An[yy, xx] = picture[y][x]
    if height > width:
        for y in range(N, height):
            for x in range(N):
                An[y][x] = picture[y][x]
    elif height < width:
        for y in range(N):
            for x in range(N, width):
                An[y][x] = picture[y][x]
    return An

def watermark(picture):
    index = 0
    for i in range(RowRange):
        for j in range(ColRange):
            a = picture[i, j]
            digit = info[index]
            index += 1

            if a[1] % 2 == 0 and digit == 1: #Check if the LSB in of the green color chanel in a is even and if the actual bit in the watermark is '1'
                a[1] = a[1] + 1

            elif a[1] % 2 == 1 and digit == 0: #Check if the LSB in of the green color chanel in a is odd and if the actual bit in the watermark is '0'
                a[1] = a[1] - 1
            picture[i, j] = a

def sha_extract(picture):
    s = ''
    count = 1
    num = 0
    for i in range(RowRange):
        for j in range(ColRange):
            if count == 4:
                count = 1
                num = num * 2 + picture[i, j][1] % 2
                if num <= 9:
                    s = s + chr(int(num + 48))
                else:

                    s = s + chr(int(num + 87))
                num = 0
            else:
                num = num * 2 + picture[i, j][1] % 2
                count += 1
    return s

## MAIN ##
print("Digital Watermarking - Example 1")
option=1
while option != 0:
    option = input("\t1 - Watermark Embedding\n\t2 - Watermark Extracting\n\t0 - exit\n\t>> ")
    if option == '1':
        imagePath = input("Path of the image to be embeded: ")
        #DEBUG1
        imagePath = "Original Images\\dog.png"
        id = input("ID: ")
        #DEBUG
        id="Some I Want"

        sha, info = hash(id)
        img = cv.imread(imagePath)
        height = img.shape[0]
        width = img.shape[1]

        p1 = arnold(img)
        cv.imwrite("Watermarked Images\\dog_wt2-1.png", p1)
        watermark(p1)
        cv.imwrite("Watermarked Images\\dog_wt2-2.png", p1)
        p2 = recover(p1)
        cv.imwrite("Watermarked Images\\dog_wt2.png", p2)
    elif option == '2':
        imagePathD = input("Path of the image to extract: ")
        #DEBUG1
        imagePathD = "Watermarked Images\\dog_wt2.png"
        idD = input("ID: ")
        #DEBUG
        idD="What I Want"

        sha, info = hash(idD)
        img = cv.imread(imagePathD)
        height = img.shape[0]
        width = img.shape[1]

        if sha == sha_extract(arnold(img)):
            print(sha)
            print(sha_extract(arnold(img)))
            print("Copyright verified successfully")
        else:
            print(sha)
            print(sha_extract(arnold(img)))
            print("Copyright verified unsuccessfully")
    elif option == '0':
        sys.exit()