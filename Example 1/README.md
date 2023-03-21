# Digital Watermarking - Example 1

## Introduction
This is a really simple example of how digital watermark works. Basically this code implements a simple digital watermarking algorithm using <bold>LSB steganography</bold>. The user can choose between
- embedding a watermark in an image
- extracting the watermark from a watermarked image

## Example of Execution
As an example we will encrypt the message `Here goes the watermark` in an example image that is under the Original Images folder. The original image is that one:<br/>
![Original Image](/ReadMe%20Images/dog.png)<br/>
After that process we will get the watermarked image, that looks like that::<br/>
![Watermarked Image](/ReadMe%20Images/wt_dog.png)<br/>
Extracting the watermark will result in the following output:<br/>
![Output in Terminal](/ReadMe%20Images/output.png)<br/>

## Code Summary
The code as three main functions that are:<br/>
* `checkImageFormat(img)`: this function checks if the image format is .png. If the image is not a .png, it prints a message and exits the program.

* `embedding_info(picname, savename, text)`: this function takes the path of an image, the path to save the watermarked image and a text to be embedded in the image. The function first reads the image and initializes some variables. It then converts each character of the text into a binary string (each character will have 16 bits) and stores the bits in an array. The array will have the following structure and we can get the watermark text from it:<br/> 
![Array of bits](/ReadMe%20Images/array.png)<br/>
The LSB of each color component of each pixel in the image is replaced with one bit of the text until all the text has been embedded. The watermarked image is saved in the path specified by savename.<br/>
Just for debug, and only for this document I put all the pixeis that contain the watermark in black. This is to be easier to understand how the watermaked is located.<br/>
![Watermarked Image - Debug](/ReadMe%20Images/wt__dog.png)<br/>

* `extract_info(picname)`: this function takes the path of a watermarked image as input. The function reads the image and initializes some variables. It then iterates over each pixel in the image and extracts the LSB of each color component. The extracted bits are stored in an array until a full character has been extracted. The binary string is then converted into an ASCII character and added to a text string until the end of the text is reached. The function stops when it detects the end of the flag, which is represented by `#%#`.

In the main function the code will iterate over a loop that allows the user to select between embedding or extracting a watermark, if some of this options are not chossen the program will exit.<br/>

## Resume
Overall, this code provides a good starting point for a simple digital watermarking algorithm, but would need to be further developed and tested to be used in a production environment.