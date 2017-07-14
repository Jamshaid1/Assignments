import requests
import time
from bs4 import BeautifulSoup

link_list=[]
new_links=[]
unique_links=[]

thefile = open('urls.txt', 'w')

  
def write_urls(url,delay,no_of_urls):
        link_list=[]
        time.sleep(delay)
        response  = requests.get(url)
        if response.status_code == 200:
           data = response.content
           soup = BeautifulSoup(data,"lxml")
           for link in soup.find_all('a'):
               if len(link_list) < no_of_urls and link.get('href'):
                  if link.get('href')[0]=='h' and link.get('href') not in link_list:
                     link_list.append(link.get('href'))
                  else:
                     link_list.append("%s%s" % (url,link.get('href')))
        for i in link_list:
            if i not in unique_links:
               unique_links.append(i)
        for links in unique_links:
            thefile.write("%s\n" % links)   


def crawls_website(url,delay,no_of_urls):
    write_urls(url,delay,no_of_urls)
    new_links=link_list
    for links in new_links:
        write_urls(links,delay,no_of_urls)
    input_file = open('urls.txt', "r")
    for line in input_file:
        unique_links.append(line)
    
    print "total number of unique pages visited: %s" % len(unique_links)


if __name__ == "__main__":
     
    crawls_website("https://www.google.com",3,100)
    
  


