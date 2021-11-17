import os
import requests
from PIL import Image 
from io import BytesIO
from Crypto.Cipher import AES 
from .data_hiding import decode, encode 


PATH = os.getcwd()+'/media/'

def pad(data): 
    return data + b"\x00"*(16-len(data)%16)  
 
def convert_to_RGB(data): 
    r, g, b = tuple(map(lambda d: [data[i] for i in range(0,len(data)) if i % 3 == d], [0, 1, 2])) 
    pixels = tuple(zip(r,g,b)) 
    return pixels 
     
def process_image(Img,key): 
    print(Img.image.url)
    response = requests.get(Img.image.url)
    im = Image.open(BytesIO(response.content)) 
    
    decoded_data=''
    if Img.type.startswith('encrypt'):
        im = encode(Img.image.url,Img.message)
        

    data = im.convert("RGB").tobytes()  
    
    original = len(data)  
    key=str(key)
    secrete_key=key[0:32]
    IV = key[0:16]

    if Img.type=='encrypt_cbc':
        new = convert_to_RGB(aes_cbc_encrypt(secrete_key, pad(data),IV)[:original]) 
    elif Img.type=='encrypt_ecb':
        new = convert_to_RGB(aes_ecb_encrypt(secrete_key, pad(data))[:original])
    elif Img.type=='decrypt_ecb':
        new = convert_to_RGB(aes_ecb_decrypt(secrete_key, pad(data))[:original])
    else:
        new = convert_to_RGB(aes_cbc_decrypt(secrete_key, pad(data),IV)[:original])  
    
    im2 = Image.new(im.mode, im.size) 
    im2.putdata(new) 
    
    if Img.type.startswith('encrypt'):
        im2.save(PATH+'encrypted_'+Img.name+'.png','png')
    else:
        im2.save(PATH+'decrypted_'+Img.name+'.png','png')
    

    if Img.type.startswith('decrypt'):    
        decoded_data=decode(PATH+'decrypted_'+Img.name+'.png')

    return decoded_data

def aes_cbc_encrypt(key, data,IV, mode=AES.MODE_CBC): 
    aes = AES.new(key.encode("utf8"), mode, IV.encode("utf8")) 
    new_data = aes.encrypt(data) 
    return new_data 
def aes_ecb_encrypt(key, data, mode=AES.MODE_ECB): 
    aes = AES.new(key.encode("utf8"), mode) 
    new_data = aes.encrypt(data) 
    return new_data 
 
def aes_cbc_decrypt(key, data,IV, mode=AES.MODE_CBC):
    aes = AES.new(key.encode("utf8"), mode, IV.encode("utf8")) 
    new_data = aes.decrypt(data)
    return new_data

def aes_ecb_decrypt(key, data, mode=AES.MODE_ECB): 
    aes = AES.new(key.encode("utf8"), mode) 
    new_data = aes.decrypt(data) 
    return new_data 

