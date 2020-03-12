#  Tic Toc function is to find the time it takes for program to excecute 
#  tic() starts the clock and toc() stop the clock and report the duration
import os, ssl

def tic():
    #Homemade version of matlab tic and toc functions
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()
 
def toc():
    import time
    if 'startTime_for_tictoc' in globals():
        print("Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds.")
    else:
        print("Toc: start time not set")

# Split string is homemade fuction to break strings into words and return the words in a list format  
# Splitlist can be any list of charatcters that in a normal not can separate two words. 
# Example : splitlist = '-! <>)(?,.""'
        
def split_string(source,splitlist):
    words = []
    atsplit=True
    if type(source)!=str or type(source)!=str:
        for ee in source:
            e = ee.encode('ascii', 'ignore')
            if len(e)<50:
                for char in e:
                    if char in splitlist:
                        atsplit = True
                    else:
                        if atsplit:
                            words.append(char)
                            atsplit=False
                        else:
                            words[-1]=words[-1]+char
    else:
        for char in source:
            if char in splitlist:
                atsplit = True
            else:
                if atsplit:
                    words.append(char)
                    atsplit=False
                else:
                    words[-1]=words[-1]+char



    return words

# Version 2
def split_string2(source,splitlist):
    words = []
    atsplit=True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                words.append(char)
                atsplit=False
            else:
                words[-1]=words[-1]+char



    return words

# Section 2
# Getting the content of a webpage from internet



def get_page3(url):
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    from bs4.element import Comment
    def tag_visible(element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    def text_from_html(body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = list(filter(tag_visible, texts))  
        return " ".join(t.strip() for t in visible_texts)
        
    html = urlopen(url).read()
    #print(text_from_html(html))
    return text_from_html(html)

# get_page2(url) clean the recieved content from website from HTML, JAVA scripts and so on using BeautifulSoup and return the Text content only
def get_page2(url):
    try:
        
        from urllib.request import urlopen
        resp = urlopen(url).read()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(resp,'html.parser')
        data = soup.findAll(text=True)
        return resp,data
    except:
        return "",""
    return "",""

# get_page(url) return the raw content of the page that may includes HTML, JAVA scripts and so on.  
def get_page(url):
    try:
        
        from urllib.request import urlopen
        resp = urlopen(url).read()
        return resp
    except:
        return ""
    return ""

# request function  
def request_page(url):
    import requests
    return requests.get(url).content

#Count the words and report them in dictionary
def word_count(w,worg):
    if w in list(worg.keys()):
        worg[w]=worg[w]+1
    else:
        worg[w]=1
    return worg

def worgIt(pageUrl):
    words, textOnly=content2ListText(pageUrl)
    worg = {}
#### I used rawContent it works more accurately on pages like bbc, cnn and so on that have lots of cosmetic scripts
    for w1 in words:
        w2=[]
        if w1.find('\n')==-1:
            worg=word_count(w1,worg)
        else:
            w2=[_f for _f in w1.strip().split("\n") if _f]   
            if len(w2)>0:
                for w in w2:
                    worg=word_count(w,worg)
    return worg, textOnly
# get page content and create a list = ['html/java/etc words in continous string', 'TXT words in continous string']
def content2ListText(pageUrl):
    content = get_page3(pageUrl)
    sList = "-! <>)(?,._1234567890+-/\~|][$%^&*#@`}{;:='"+'"'
    W = [];
    W = split_string(content,sList)
    return W, content

#search within worg dictionary
def wS(wordOfInterest, worg):
    print("*****************************1**********************************")
    print(' how many times word "',wordOfInterest,'" was seen in the URL')
    print(worg.get(wordOfInterest.lower(),0))
    print("*****************************2********************************")
    return
   
#------  Code main Body Starts here -------- 3
#------  Code main Body Starts here -------- 2
#------  Code main Body Starts here -------- 1


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

def worging(pageUrl, wordOfInterest):
    #pageUrl = "https://www.aljazeera.com"
    worg, textOnly = worgIt(pageUrl)
    worgList=list(worg.keys())
    worgN=[]
    wList=[]
    text=''
    for i in worgList:
        Q=worg[i]
        worgN.append(Q)
        wList.append([i,Q])
        text= text + (i+' ')*Q

    #wordOfInterest="Coronavirus"
    wS(wordOfInterest, worg)   
    #print worg
    #import operator
    #sorted_x = sorted(worg.items(), key=operator.itemgetter(0))
    #print sorted_x
    import matplotlib.pyplot as plt
    
    #plt.plot(worgList, worgN)
    import operator
    index, value = max(enumerate(worgN), key=operator.itemgetter(1))
    
    for i in worgList:
        if worg[i]>50 and worg[i]<100:
            print(i, worg[i])

    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
    wordcloud = WordCloud().generate(textOnly)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
