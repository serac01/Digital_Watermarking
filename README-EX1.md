# Digital Watermarking - Example 1
This first example will encrypt a message given from the user in an image.<br/> As an example I chossed the image below and the text for the watermark: `Some text`.<br/>
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