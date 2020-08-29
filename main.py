import requests
import numpy as np
from PIL import Image 
from twilio.rest import Client

def get_sunset(self):
    pass
    url = 'https://sunsetwx.com/sunset/sunset_et.png'
    r = requests.get(url, allow_redirects=True)

    open('/tmp/sunset.png', 'wb').write(r.content)
    
    # Importing Image class from PIL module 
    from PIL import Image 

    # Opens a image in RGB mode 
    im = Image.open("/tmp/sunset.png") 

    # Size of the image in pixels (size of orginal image) 
    # (This is not mandatory) 
    width, height = im.size 
    
    # Setting the points for cropped image 
    # I set to Ohio
    left = 930
    top = 470
    right = 970
    bottom = 510

    # Cropped image of above dimension 
    # (It will not change orginal image) 
    sw_ohio = im.crop((left, top, right, bottom)) 

    # Shows the image in image viewer 
    #sw_ohio.show() 
    #sw_ohio.save('sw_ohio.png')
    
    red_value = (np.asarray(sw_ohio)[..., 0].mean())
    
    if red_value > 100:
        flag = True
        print("Flag is True!")
    else:
        flag = False
        print("Flag is False.")
        
    
    # the following line needs your Twilio Account SID and Auth Token
    client = Client("xxx", "xxx")

    if flag == True:
        client.messages.create(to="+xxx", 
                               from_="+xxx", 
                               body="There's gonna be a good sunset in your area!! The red value is: {} Check it: https://sunsetwx.com/sunset/sunset_et.png".format(red_value))