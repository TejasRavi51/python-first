import os
import requests
import shutil
from download_util import download_file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

downloaded_img_path = os.path.join(DOWNLOAD_DIR, '1.jpg')
url = "https://thehappypuppysite.com/wp-content/uploads/2018/10/beagle-and-puppies.jpg"

#a smallish item
r = requests.get(url,stream=True)
r.raise_for_status() # error if not 200
with open(downloaded_img_path, 'wb') as f:
    f.write(r.content)

#dl_filename = os.path.basename(url)
#new_dl_path = os.path.join(downloads_dir, dl_filename)
#with requests.get(url, stream=True) as r:
#    with open(new_dl_path, 'wb') as file_obj:
#        shutil.copyfileobj(r.raw, file_obj)


#for larger files    
download_file(url, DOWNLOAD_DIR)