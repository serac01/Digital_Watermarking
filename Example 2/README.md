# Digital Watermarking - Example 2
This example will encrypt a message given from the user in an image.<br/> As an example I chossed the image below and the ID for the watermark is `What I Want`.<br/>
![This is an image](/ReadMe%20Images/dog.png)
## Encryption
To embedded the text in the image, we will use the arnold method to shuffle all the pixeis. In the end the image will be something like that:<br/>

![This is an image](/ReadMe%20Images/dog_arnold.png)
<br/>
Then we apply the watermark in the LSB in the create a hash using the SHA-256 method and in the end we will get a string with 256 bits.<br/>
![This is an image](/ReadMe%20Images/dog_wtarnold.png)
<br/>
Note: the blue and red pixeis are just for debug!<br/>
Now that we have the ID in the image we will recover the image and it will look like that:<br/>
![This is an image](/ReadMe%20Images/dog_recover.png)

Note: the blue and red pixeis are just for debug!
## Decryption
To decrypt we will ask the user for the image with the watermark and the ID. The result will return if the ID match with the watermark in the image or not.<br/>
First we will generate the hash for the new ID (is the same function as before). Then we will use the arnold method for the image, to be easier to get the watermark, and the when we get the ID from the watermark, we will compare the results and say if it's the same ID or not.<br/>
![This is an image](/ReadMe%20Images/result.png)


