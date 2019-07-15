import urllib
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from random import randint
import time
import re
import json
import datetime
import os
import requests
from pandas.io.json import json_normalize
import pandas as pd, numpy as np


username = input("Enter account name: ")
posts = input("Enter number of posts: ")
posts = int(posts) // 7
linklength= 1
picturelength = 1
links=[]
directory="/home/john/Desktop/gr.ai.tful/pics/"
pictures=[]
browser = webdriver.Chrome('/home/john/Desktop/graitful/chromedriver')
browser.get('https://www.instagram.com/'+username+'/?hl=en')
for i in range(0,posts//5):
    print("Outside loop: "+str(i+1)+" OUT OF: "+str(posts//5))
    for x in range(0,4):
        print("Inside loop: "+str(x+1)+" OUT OF: 4")
        Pagelength = browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(randint(5,17))
    try:
        print("test")
        source = browser.page_source
        data=BeautifulSoup(source, 'html.parser')
        body = data.find('body')
        script = body.find('span')
        for pic in script.findAll('a'):
            if re.match("/p", pic.get('href')):
               links.append('https://www.instagram.com'+pic.get('href'))
        length = len(links)
        linklength = linklength + length
        print("test1")
        links = list(dict.fromkeys(links))
        time.sleep(randint(2,10))
        for i in range(len(links)):
            print(str(i+1)+" LINKS CONVERTED "+str(datetime.time()))
            time.sleep(randint(3,19))
            try:
                page = urlopen(links[i],timeout=10).read()
                
                data=BeautifulSoup(page, 'html.parser')
                for pic in data.findAll("meta", attrs={'content' : re.compile("^https://scontent")}):
                    pictures.append(pic['content'])
            except Exception as e:
                pass
        links.clear()
        picturelength= picturelength + len(pictures)
        for i in range(len(pictures)):
            print(str(i+1)+" IMAGES DOWNLOADED "+str(datetime.time()))
            time.sleep(randint(2,12))
            try:
                urllib.request.urlretrieve(pictures[i], directory+str(i+picturelength)+".jpg")
            except Exception as e:
                pass
        pictures.clear()   
        time.sleep(randint(2,10))
    except Exception as e:
        pass




#source = browser.page_source
#data=BeautifulSoup(source, 'html.parser')
#body = data.find('body')
#script = body.find('span')
#for pic in script.findAll('a'):
#    if re.match("/p", pic.get('href')):
#        links.append('https://www.instagram.com'+pic.get('href'))


#time.sleep(randint(2,10))

#Pagelength = browser.execute_script("window.scrollTo(0,document.body.scrollHeight/1.5,document.body.scrollHeight/3.0);")

#source = browser.page_source
#data=BeautifulSoup(source, 'html.parser')
#body = data.find('body')
#script = body.find('span')
#for pic in script.findAll('a'):
#    if re.match("/p", pic.get('href')):
#        links.append('https://www.instagram.com'+pic.get('href'))


#directory="/home/john/Desktop/graitful/pics/"
#links = list(dict.fromkeys(links))
#pictures=[]
#length = len(links)
#print(str(length)+" LINKS LENGTH")
#for i in range(len(links)):
#    print(str(links[i]))
#    print(str(links[i]))
#    print(str((i/length)*100)+"% LINKS FOUND")
#    time.sleep(randint(3,19))
#    page = urlopen(links[i]).read()
#    data=BeautifulSoup(page, 'html.parser')
#    for pic in data.findAll("meta", attrs={'content' : re.compile("^https://scontent")}):
#        pictures.append(pic['content'])
#print(pictures)
#length = len(pictures)
#print(str(length)+" PICTURES LENGTH")
#for i in range(len(pictures)):
#    print(pictures[i])
#    print(str((i/length)*100)+"% IMAGES DOWNLOADED")
#    print(str(length)+" PICTURES LENGTH")
 #   time.sleep(randint(2,10))
  #  urllib.request.urlretrieve(pictures[i], directory+str(i)+".jpg")




