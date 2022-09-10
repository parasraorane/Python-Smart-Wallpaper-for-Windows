import requests,ctypes,os,numpy as np
from PIL import Image,ImageFont,ImageDraw

z=os.listdir("path/to/folder/containing/wallpapers/")

#opening random image
path=z[np.random.randint(len(z))]
z=Image.open(z+path)

try:#write a quote on the image if it is fetched succesfully
    I1 = ImageDraw.Draw(z)
    myFont = ImageFont.truetype("path/to/the/font/.ttf/file",int(20*z.size[0]/1920))
    l="http://api.quotable.io/random"
    r=requests.get(l)
    r=r.json()
    text=r["content"]+" - "+r["author"]
    I1.text((10,z.size[1]-int(20*z.size[0]/1920)-20), text, font=myFont, fill =(255, 255, 255))
except:
    True
    
try:#save as jpg
    path="path/to/save/the/wallpaper/with/quotes/in/jpg/format.jpg"
    z.save(path)
except:#or save as png
    path="path/to/save/the/wallpaper/with/quotes/in/png/format.png"
    z.save(path)
ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)