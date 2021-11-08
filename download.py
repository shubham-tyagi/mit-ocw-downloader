import urllib.request
import sys
import re
from html.parser import HTMLParser
import time 

links=0
src=[]
base_url='https://ocw.mit.edu'
video_links=[]

#this function helps to print how much percent of particular video lecture is downloaded
def progress(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 100 / totalsize
        sys.stdout.write("\r %5.1f%%,   %d MB /%d MB "%(percent,(readsofar/(1024*1024)),(totalsize/(1024*1024))))
        sys.stdout.flush()
        if readsofar >= totalsize: # near the end
           print("\n")
   
#this class handles the main course page
class MyLectureParser(HTMLParser):
    def handle_starttag(self,tag,attributes):
        global links
        global src
        flag=0
        if tag=='a':
            for(key,value) in attributes:
                if key=='class' and value=='bullet medialink' :
                    links=links+1
                    flag=1

                if flag==1 and key=='href' and value:
                    
                    src.append(value)

#this class handles all the video lectures page fetched from lecture parser page
class myVideoParser(HTMLParser):
    def handle_starttag(self,tag,attributes):
        if tag=='a' :
            for(key,value) in attributes:
                # val=value.split
                if (key=='href' and value.endswith('mp4')):
                    flag=0
                    if(value in video_links):
                        flag=1
                    
                    if flag==0:
                        print (value)
                        video_links.append(value)


def open():
    
    url=input("enter the course url(copy it from the brwowser) : ") #url of the course is entered 

    if( url.find('index.htm') != -1):
        url=url.replace('index.htm','/lecture-videos')
    if(url.find('video')==-1):
        print("\ngive me the link for video pages of an mit course\n")
        return

    print (url)
    
    f=urllib.request.urlopen(url) #opens the url

    html=f.read().decode('utf-8', 'ignore') #translate the open url html page which are utf-8 encoded to 
                                            #  binary strings which machines could understand
                                            #   and ignore the characters that are not able to be converted


    parser=MyLectureParser()    #good to make HTML parser a subclass
    parser.feed(html)           #list of video lectures url page are fetched 
    video_lecture=myVideoParser()

#this for loop loops over every video lecture url and retrives the video url to be downloaded 
   
    for lecture_url in src:
        lecture_url=base_url+lecture_url
        g=urllib.request.urlopen(lecture_url)
        html1=g.read().decode('utf-8','ignore')
        video_lecture.feed(html1)   #video url is fetched for the given lecture number 
     
    


open()  
print(len(src)) 
print(len(video_links))
num=0


for video_link in video_links:
    num=num+1
    string='video'+str(num)+'.mp4'
    urllib.request.urlretrieve(video_link,string,progress) 

num=0

