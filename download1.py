import urllib.request
import urllib

def open():
    url="https://ia800308.us.archive.org/25/items/MIT16.660JIAP12/MIT16_660JIAP12_ses1-2_300k.mp4"
    file_name='video.mp4'
    urllib.request.urlretrieve(url,file_name)


open()