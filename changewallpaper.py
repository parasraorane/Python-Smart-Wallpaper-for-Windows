import requests,ctypes,os,numpy as np
from PIL import Image,ImageFont,ImageDraw
import yfinance as yf

#adding tickers
#list of tuples with first element as the ticker name from yahoo finance and second as the name to display in the wallpaper
tickers=[("^GSPC","s&p500"),
         ("aapl","aapl"),
         ("tsla","tsla"),
         ("^nsei","nf50"),
         ("^nsebank","nfbnk"),
         ("reliance.ns","ris"),
        ("tcs.ns","tcs"),
        ("infy.ns","infy"),
        ("BTC-USD","btc")]

#function to pad wallpaper in correct resolution
def add_margin(img,top,left,bottom,right,color):
    width, height = img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(img.mode, (new_width, new_height),color)
    result.paste(img, (left, top))
    return result
#function to convert image to correct size
def conv_to_size(path,path_to_save=None):
    z=Image.open(path)
    if z.size[0]/1920>z.size[1]/1080:
        vres=z.size[0]*1080/1920
        vres=vres-z.size[1]
        vres=int(vres/2)
        res=add_margin(z,vres,0,vres,0,(0,0,0))
    else:
        hres=z.size[1]*1920/1080
        hres=hres-z.size[0]
        hres=int(hres/2)
        res=add_margin(z,0,hres,0,hres,(0,0,0))
    if path_to_save is not None:
        res.save(path_to_save)
    else:
        res.save(path)
#function that takes ticker and returns 24hr change and current price rounded to 2 decimals
def ret_change(ticker):
    x= yf.Ticker(ticker)
    z=x.history(period="3d")
    return (((z.iloc[-1]["Close"]-z.iloc[-2]["Close"])/z.iloc[-2]["Close"])*100).round(2),z.iloc[-1]["Close"].round(2)

z=os.listdir("path/to/folder/containing/images")

#opening random image
path="path/to/folder/containing/images"+z[np.random.randint(len(z))]
z=Image.open(path)

#ensure the ratio of dimensions for wallpaper is correct
if z.size[0]/z.size[1]>1.78 or z.size[0]/z.size[1]<1.76:
    conv_to_size(path)
    z=Image.open(path)
z=z.resize((1920,1080))

try:#write a quote on the image if it is fetched succesfully
    I1 = ImageDraw.Draw(z)
    myFont = ImageFont.truetype("path/to/.ttf/font/file",20)
    l="http://api.quotable.io/random"
    r=requests.get(l)
    r=r.json()
    text=r["content"]+" - "+r["author"]

    I1.text((10,1050), text, font=myFont, fill =(255, 255, 255))
    
    #displaying tickers
    ticpos=10
    for i,j in tickers:
        chn,pc=ret_change(i)
        I1.text((1670,ticpos),j, font=myFont, fill =(255,255,255))
        if chn>=0:
            I1.text((1750,ticpos),str(chn)+"%", font=myFont, fill =(0,255,0))
            I1.text((1830,ticpos),str(pc), font=myFont, fill =(0,255,0))
        else:
            I1.text((1750,ticpos),str(abs(chn))+"%", font=myFont, fill =(255,0,0))
            I1.text((1830,ticpos),str(pc), font=myFont, fill =(255,0,0))
        ticpos+=25
except:
    True
    
try:#save as jpg
    save_path="path/to/save/temp/wallpaper/in/.jpg/format"
    z.save(save_path,quality="high")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, save_path, 0)
except:#or save as png
    save_path="path/to/save/temp/wallpaper/in/.png/format"
    z.save("D:/Pictures/temp.png",quality="high")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, save_path , 0)