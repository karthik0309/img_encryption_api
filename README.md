
### Heroku app - [here](https://gentle-bayou-32067.herokuapp.com/)

# ImgCrypt (image encryption and reversible data-hidiing)
    The use of the internet and wireless communications has been rapidly growing andoccupying a wide__ area in everyday life.
    Millions of users generate and interchange large amount of electronic data on a daily basis in diverse domains. However,
    the issue of privacy and security is on the top of the crucial concerns which determine the diffusion of such applications 
    into the daily life. Hence, cryptography turns to become the key for the reliability and effectiveness of the embedded

## AES
    The Advanced Encryption Standard (AES) algorithm is a symmetric block cipher that processes image which is of blocks size 
    128 bits using three different cipher key size of lengths 128,192 or 256 bits. Based on the key size length used, the number 
    of execution rounds of the algorithm is 10,12 or 14 respectively. The proposed system consists of block size of 128 bits and 
    key size of 256 bits. The algorithm is applied for both image encryption and decryption. As the key size is of 256 bits it 
    will take 14 rounds.

## Data Hiding
    Hiding information in an image in a way that does not affect the original cover image pixels or cause a permanent distortion 
    after extracting that information is known as reversible data hiding technology.These schemes are developed to ensure digital 
    images' authenticity and integrity without any distortion on the original images. They guarantee that any attempt to change the 
    watermarked image will be detected by the image owner.

    In this project we are hiding information in boundary of image, where the given message is converted into ASCII and converted to 
    binary. Now we ake 3 pixels at a time(because images are mad of 3 pixels RGB), if the binary bit from message id 0 we convert the 
    pixel to even else we convert pixel to odd.The last pixel is always set to even.

    Now when we decode the image, look for th last odd pixel because thats going to be end of message.
    and apply reverse enoding to get the message.

## EndPoints
- User - /users
- Images - /Images
- modes - (AES CBC,AES EBC)
