import requests
import time
from bs4 import BeautifulSoup

link_list=[]
unique_links=[]
content_size=0 #in bytes
thefile = open('urls.txt', 'w')

  
def get_urls(url,delay,no_of_urls):
    link_list=[]
    time.sleep(delay)
    response  = requests.get(url)
    if response.status_code == 200:
       data = response.content
       global content_size
       content_size += len(data)
       soup = BeautifulSoup(data,"lxml")
       for element in soup.find_all('a'):
	   if element.get('href'):
              link = element.get('href')
              if link[0]=='h':
                 link_list.append(link)
              else:
                 link_list.append("%s%s" % (url,link))
    for i in link_list:
        if i not in unique_links and len(unique_links) < no_of_urls:
           unique_links.append(i)

def crawls_website(url,delay,no_of_urls):
    get_urls(url,delay,no_of_urls)
    
    for links in unique_links:
        if len(unique_links) < no_of_urls:
           get_urls(links,delay,no_of_urls)
    
    for links in unique_links:
        thefile.write("%s\n" % links) 

    
    print "unique pages visited: %s and downloaded content size: %s" % (len(unique_links),content_size)


if __name__ == "__main__":
     
    crawls_website("https://www.gmail.com",2,150)
   
