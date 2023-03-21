# Digital Watermarking - Example 2
## Introduction
The code implements a simple digital watermarking technique, specifically a technique that embeds a binary watermark into the least significant bit (LSB) of the green channel of an image. The user can choose between
- embedding a watermark in an image
- extracting the watermark from a watermarked image

## Example of Execution
As an example we will encrypt the message `Original Watermark` in an example image that is under the Original Images folder. The original image is that one:<br/>
![Original Image](/ReadMe%20Images/dog.png)<br/>
After that process we will get the watermarked image, that looks like that::<br/>
![Watermarked Image](/ReadMe%20Images/wt_dog.png)<br/>
Extracting the watermark will result in the following output:<br/>
![Output in Terminal](/ReadMe%20Images/output_2.png)<br/>

## Code Summary
The code has five main functions that are:<br/>
* `hash(ID)`: this function takes an ID string as input, generates its SHA-256 hash and converts it to binary. It then returns a list containing the original ID string and the binary representation of its SHA-256 hash.

* `arnold(picture)`: this function implements the Arnold cat map to shuffle the pixels in the input image. It takes a numpy array representing the input image and returns another numpy array with shuffled pixels.<br/>
After this process the image will be like that:
![Output in Terminal](/ReadMe%20Images/dog_arnold.png)<br/>

* `watermark(picture)`: this function embeds a binary watermark into the input image by changing the least significant bit (LSB) of the green color channel in each pixel. It takes a numpy array representing the input image as input and modifies it in place.<br/>
This function will be executed after the arnold function, and just for debug I put the pixels that contain the watermark red. After this process the image will be like that:
![Output in Terminal](/ReadMe%20Images/dog_arnold_wt.png)<br/>

* `recover(picture)`: this function performs the inverse operation of arnold() to recover the original image from a shuffled image. It takes a numpy array with shuffled pixels as input and returns the original image.<br/>
This function will be executed after the watermark function, and just for debug I put the pixels that contain the watermark red. After this process the image will be like that:
![Output in Terminal](/ReadMe%20Images/dog_wt.png)<br/>

* `sha_extract(picture)`: this function extracts the watermark from the input image by reading the LSB of the green color channel in each pixel and reconstructing the original binary watermark. It takes a numpy array representing the input image and returns the reconstructed binary watermark as a string.<br/>

The main program gives the user the option to embed a watermark into an image or extract a watermark from an image. Depending on the option chossed, it will perfome the functions above.

## Resume
Overall, this code provides a good starting point for a simple digital watermarking algorithm, but would need to be further developed and tested to be used in a production environment.
