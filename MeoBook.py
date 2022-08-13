import urllib.request
import urllib, re, requests, os
from bs4 import BeautifulSoup
from pprint import pprint
import json

def replace_key(key):
    return urllib.parse.quote(key, safe='')

class MeoBookError(Exception):
    pass

class Book:
    """
        Book object

    """
    def __init__(self, title, description, link, filetype='pdf'):
        self.title = title
        self.description = description
        self.link = link
        self.filetype = filetype
    
    def __repr__(self):
        return "Book "+str(self.title)
    
    def __str__(self):
        return self.title
    
    def download(self, directory:str):
        """
            Method to download the book in a directory
        """
        r = requests.get(self.link)
        
        if os.path.exists(directory):

            with open(os.path.join(directory, self.title+'.'+self.filetype), 'wb') as file:
                file.write(r.content)
        else:
            raise MeoBookError(f"This path {directory} does not exists")
        

class MeoBook():
    def __init__(self):
        pass
    
    def search_book(self, keyword:str, filetype='pdf') -> list:
        item = {}
        rslt = []

        url = f'https://google.com/search?q={replace_key(keyword)+filetype}'

        # Perform the request
        request = urllib.request.Request(url)

        # Set a normal User Agent header, otherwise Google will block the request.
        request.add_header(
            'User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
        raw_response = urllib.request.urlopen(request).read()

        # Read the repsonse as a utf-8 string
        html = raw_response.decode("utf-8")

        soup = BeautifulSoup(html, 'html.parser')
        divs = soup.select("#search div.g")
        i = 0
        for div in divs:
            # Search for a h3 tag
            title_raw = div.select("h3")
            link_raw = div.select("a")
            
            content_raw = div.find(class_='VwiC3b')
            # print(content_raw.get_text())   
            # print(link_raw[0]['href'])

            # Check if we have found a result
            try:
                if (len(title_raw) >= 1 and len(link_raw) >= 1 ):

                    # Print the title
                    h3 = title_raw[0]
                # print(h3.get_text())
                    item['title'] = h3.get_text()
                    item['link'] = link_raw[0]['href']
                    print(item['link'])
                    item['content'] = content_raw.get_text()
                    # try:
                    #     item['favicon'] = favicon.get(item['link'])[0].url
                    # except:
                    item['favicon'] = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
                    
                    b = Book(item['title'], item['content'], item['link'])
                    if item['link'].endswith('.'+filetype):rslt.append(b)
                    i += 1
                    item = {}
            except Exception as e:
                print(e)
            # if i == 8: break

        # pprint(rslt)
        return rslt
