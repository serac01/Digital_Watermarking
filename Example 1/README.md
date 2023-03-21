# Digital Watermarking - Example 1

## Introduction
This is a really simple example of how digital watermark works. Basically this code implements a simple digital watermarking algorithm using <bold>LSB steganography</bold>. The user can choose between
- embedding a watermark in an image
- extracting the watermark from a watermarked image

## Example of Execution
example will encrypt a message given from the user in an image.<br/> As an example I chossed the image below and the text for the watermark: `Some text`.<br/>
![This is an image](/ReadMe%20Images/dog.png)
## Encryption
To embedded the text in the image, we will add a flag in the end of the message given from the user that is `#%#`, to be easier when we are trying to decript the image.<br/>
Then, we will convert each chacarter to a binary with 16 bits.
<br/>
Now that we have the generated text in binary, we will use the LSB of the first pixels in the image to encript the text.<br/>
In the end we will have our encrypted image will be something like that:<br/>

![This is an image](/ReadMe%20Images/dog_wt.png)

In this case, I put the pixels in black (just for debug)<br/>
![This is an image](/ReadMe%20Images/amplified.png)
## Decryption
To extract the information we will do the reverse process.
We will iterate over each pixel and append the LSB to a string, when we got 16 bits, we will convert the text the binary string to an ASCII character and append to another string. When we got a string which the last 3 characters are `#%#`, we assume that we already got the text and the process is finished.<br/>
![This is an image](/ReadMe%20Images/array.png)

## Code Summary
The code as three main functions that are:<br/>
* `checkImageFormat(img)`: this function checks if the image format is .png. If the image is not a .png, it prints a message and exits the program.

* `embedding_info(picname, savename, text)`: this function takes the path of an image, the path to save the watermarked image and a text to be embedded in the image. The function first reads the image and initializes some variables. It then converts each character of the text into a binary string and stores the bits in an array. The LSB of each color component of each pixel in the image is replaced with one bit of the text until all the text has been embedded. The watermarked image is saved in the path specified by savename.

* `extract_info(picname)`: this function takes the path of a watermarked image as input. The function reads the image and initializes some variables. It then iterates over each pixel in the image and extracts the LSB of each color component. The extracted bits are stored in an array until a full character has been extracted. The binary string is then converted into an ASCII character and added to a text string until the end of the text is reached. The function stops when it detects the end of the flag, which is represented by `#%#`.

In the main function the code will iterate over a loop that allows the user to select between embedding or extracting a watermark, if some of this options are not chossen the program will exit.<br/>

## Resume
Overall, this code provides a good starting point for a simple digital watermarking algorithm, but would need to be further developed and tested to be used in a production environment.