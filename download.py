import urllib.request
import re
from html.parser import HTMLParser



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
                    print (value)
                    src.append(value)
         

            
        # print (tag)
    # []
    # def handle_data(self,data):
    #     if data=='Video lectures':
    #         print (data)
    #         global links
    #         links=1

    #     if data.startswith("Lecture"):
            



def open():
    url="https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/index.htm"
    url=url.replace('index.htm','video-lectures')
    print (url)
    f=urllib.request.urlopen(url)
    # f=urllib.request.urlopen("new.html")
    html=f.read().decode('utf-8', 'ignore')
    # print (html)
    # f.close()         


    parser=MyLectureParser()
    parser.feed(html)
    # parser.feed("<html><head><title>HTML Parser - I</title></head>"
    #         +"<body><h1>HackerRank</h1><br /><a>hello</a></body></html>")
    # print("total links : %d" % links)


links=0
src=[]
open()  
# print(links) 
print (len(src)) 