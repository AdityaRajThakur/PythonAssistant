import ctypes
import time
import io
from PIL import Image
import requests
import json

KEY = "Ha3DDGoZc428r4JaYDai7LL1NliasmuejqWR4gg6vWw"
savepath = "C:\\Users\\Administrator\\Desktop\\api\\{id}.jpg"
url = f"https://api.unsplash.com/photos/?client_id={KEY}&query=wallpaper&orientation=landscape&topics=computer"

res = requests.get(url)

# print(res.status_code)

data  = res.json()
count = 1 
for item in data:
    if count == 5 : 
        break
    
    # print(item)
    # print(item.keys())
    print(item['links']['download'])
    # print(item['id'])
    name = item['id']
    print(f"Downloading file..... {name}")
    res  = requests.get(item['links']['download'])
    image_data = Image.open(io.BytesIO(res.content))
    savepath = f'C:\\Users\\Administrator\\Desktop\\api\\{name}.jpg'
    image_data.save(savepath)
    print("Adding the Background Wallpaper....")
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,savepath, 0)
    count+=1
    time.sleep(5)
    
    
