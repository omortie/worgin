index = {}
def tic():
    #Homemade version of matlab tic and toc functions
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    import time
    if 'startTime_for_tictoc' in globals():
        print "Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds."
    else:
        print "Toc: start time not set"

def split_string(source,splitlist):
    words = []
    atsplit=True
    if type(source)!=str:
        for e in source:
            if len(e.encode('utf-8'))<50:
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


    #print "*",words
    return words

########
#####################################
#####################################
def get_page2(url):
    try:
        
        from urllib import urlopen
        resp = urlopen(url).read()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(resp,'html.parser')
        data = soup.findAll(text=True)
        return resp,data
    except:
        #print 'Fail to open!'
        return "",""
    return "",""
    
def get_page(url):
    try:
        
        from urllib import urlopen
        resp = urlopen(url).read()
        return resp
    except:
        return ""
    return ""
    
def request_page(url):
    import requests
    return requests.get(url).content
    

#Next target is to improve that we find the right links
def get_next_target(page):
    start_link = page.find('<a href=')
#    start_link = page.find(' href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page, page_content): 
    links = [] 
    domain = domain_find(page)
    while True: 
        url, endpos = get_next_target(page_content)
        if url:
            if 'http' not in url:
                print "771", url
                url = domain + url
            links.append(url) 
            page_content = page_content[endpos:] 
        else: 
            break 
    return links

def crawl_web(index, seed, max_depth): 
    tocrawl = [seed] 
    crawled = []
    next_depth = []
    depth = 0    
#    index = {}
    num_pages = 1    
    while tocrawl and depth <= max_depth: 
        page = tocrawl.pop()
        if page not in crawled: 
            whole_content, content = get_page2(page) 
#            content = get_page(page) 
            add_page_to_index(index, page, content) 
            union(next_depth, get_all_links(page,whole_content)) 
            crawled.append(page) 
            print num_pages,'.',depth,'-', page
            print content
        num_pages -=1
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth += 1
            num_pages = len(tocrawl)
            print 'number of pages to be crowled at depth ',depth,' are ', num_pages
    return index 

def crawl_domain(index, seed, max_depth): 
    tocrawl = [seed] 
    crawled = [] 
#    index = {} 
    domain = domain_find(seed)
    print 3*'*',domain,3*'*'
    sub_domain = domain    # could have been seed
    next_depth=[]
    depth=0  
    num_pages = 1
    while tocrawl and depth <= max_depth: 
        page = tocrawl.pop()     
        if page not in crawled and sub_domain in page: 
            whole_content, content = get_page2(page) 
            add_page_to_index(index, page, content) 
            union(next_depth, get_all_links(page,whole_content)) 
            crawled.append(page) 
            print str(num_pages)+'/'+str(depth),'-', page #This line can be removed 
        num_pages -=1
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth += 1
            num_pages = len(tocrawl)
            print 'number of pages to be crowled at depth ',depth,' are ', num_pages
    return index 
    
def add_page_to_index(index, url, content): 
    #words = content.split()
    words  = split_string(content,'-! <>)(?,.""/|:~\;}{*_=^&$#@+')    
    for word in words: 
        add_to_index(index, word, url) 
    return index

def add_to_index(index, keyword, url): 
# index = {keyword1:{url1:{date1:num, date2:num2, ...},url2:{date1:num, date2:num2, ...}},Keyword2:...}
    today = date() 
    if keyword in index:
        if url in index[keyword]:
            if today in index[keyword][url]:
                index[keyword][url][today]+=1
                return index                
        index[keyword][url]={today:0}
    else:
        index[keyword] = {url:{today:0}}
    return index
        
def domain_find(url):
    if url.find('/',9)==-1:
        return url[:url.find('/',9)]+url[-1]
    return url[:url.find('/',9)]    
    
def date():
    import datetime
    today = datetime.date.today()
    return str(today)

def lookup(index, keyword): 
    if keyword in index: 
        return index[keyword] 
    else:
        return None

def print_url(index, keyword): 
#index = {keyword1:{url1:{date1:num, date2:num2, ...},url2:{date1:num, date2:num2, ...}},Keyword2:...}

    num_dict={}
    counter = 0
    if keyword in index:
        for url in index[keyword]:
            dateQ='2000-1-1'
            for date in index[keyword][url]:
                if bigger_date(date,dateQ):
                    last_date_count = index[keyword][url][date]
                    dateQ = last_date_count
                    
            counter+=1
            num_dict[last_date_count]=url
            #print counter,': ',url ,' :',last_date_count
        
        return  sorted_url(num_dict)
    else:
        return None
def sorted_url(num_dict):
    counter = 0
    a = sorted(num_dict)
    best_list=[]
    for e in a:
        counter+=1
        best_list.append(num_dict[e])
        print counter,': ',num_dict[e] ,' :',e      # printing sorted list of urls based on number of occurance 
    return best_list

def bigger_date(date,Q):
    nQ=Q.find('-')
    n=date.find('-')
    yQ=Q[:nQ]
    y=date[:n]
    mQ=Q[nQ+1:Q.find('-',nQ)]
    m=date[n+1:date.find('-',n)]
    dQ=Q[Q.find('-',nQ)+1:]
    d=date[date.find('-',n)+1:]
    if y>=yQ or (y==yQ and m>=mQ) or (y==yQ and m==mQ and d>dQ):return True
    
    return False
 
def read_index():
    import json
    # load from file:
    with open('index.json', 'r') as f:
        try:
            data = json.load(f)
    # if the file is empty the ValueError will be thrown
        except ValueError:
            data = {}
    return data

def save_index(index):
    import json    
    # save to file:
    with open('index.json', 'w') as f:
        json.dump(index, f)
    return 
def twitter_hashtag(hashtag):
    twitter_domain = 'https://twitter.com/hashtag/'
    return twitter_domain+hashtag+'?src=hash'
        ############### Write it here
def google_quest(word):
    return 'https://www.google.com/#q='+word
def inline_lookup(index):
    print "to finish type 'Exit'"
    while True:
        word_to_search = raw_input("What do you want to lookup? ")
        if word_to_search == 'Exit':
            break
        print("Here are the websites for '" + word_to_search + "'!")
        print_url(index,str(word_to_search))
    print "See you soon :)."
    return 


tic()
#tag='Iran'
#link = google_quest(tag)
#index=read_index()        # reading index from saved data source
#size = len(index)
index = crawl_web(index,"http://goolab.co/", 0)
#index = crawl_domain(index,"http://www.tabnak.com", 3)
#save_index(index)         # saving index to saved data source

    
#print lookup(index, 'Iran')
#print_url(index,'roya')
#print 5*'*','initial size:',size, len(index)-size,5*"*"
#inline_lookup(index)


toc()