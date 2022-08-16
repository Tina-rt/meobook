from pprint import pprint as pp
import urllib.request
import urllib
import requests
import os
from bs4 import BeautifulSoup


def get_file_size(url: str):
    # print(url)
    req = urllib.request.Request(url, method='HEAD')
    f = urllib.request.urlopen(req)
    return f.headers['Content-Length']


def replace_key(key):
    return urllib.parse.quote(key, safe='')


class MeoBookError(Exception):
    pass


class Book:
    """
        Book object

    """

    def __init__(self, title: str, description: str, link: str, size: int, page_number=None):
        self.title = title
        self.description = description
        self.link = link
        self.size = size
        self.size_mb = int(self.size) / 1_000_000
        self.page_number = page_number #if the page number still none, the data is not provided

    def __repr__(self):
        return f"Book {self.title} - Description : {self.description} - Number of Page: {self.page_number} - Size: {self.size} - Size MB: {self.size_mb}"

    def __str__(self):
        return f"Book {self.title} - Description : {self.description} - Number of Page: {self.page_number} - Size: {self.size} - Size MB: {self.size_mb}"


    def download(self, directory: str):
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
    """
        MeoBook Object

        Used for fetching books by searching it

        By Default, filetype will be pdf. But can be changed with self.set_file_type_epub(self) function

    """

    def __init__(self):
        self.filetype = 'pdf'

    def search_book(self, keyword: str, limit=5) -> list:
        """
            Usage : 
            search_book(keyword) return a list of Book type object
            search_book(keyword, limit=10) return a list of 10 Book type objects

            The limit parameter is not unlimited. It depends on google search. 

        """
        item = {}
        rslt = []
        for j in range(limit):

            url = f'https://google.com/search?q={replace_key(keyword)+self.filetype}&start={(j-1)*10}'

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
                if len(rslt) >= limit:
                    return rslt
                # Search for a h3 tag
                title_raw = div.select("h3")
                link_raw = div.select("a")

                content_raw = div.find(class_='VwiC3b')
                
                # Check if we have found a result
                try:
                    if (len(title_raw) >= 1 and len(link_raw) >= 1):

                        # Print the title
                        h3 = title_raw[0]
                    # print(h3.get_text())
                        title = h3.get_text()
                        link = link_raw[0]['href']

                        content = content_raw.get_text()

                        
                        if link.endswith('.'+self.filetype):
                            b = Book(title, content,
                                 link, get_file_size(link))
                            page_number = div.find(class_='wuQ4Ob')
                            if page_number:
                                b.page_number = page_number.get_text()[0]
                            
                            
                            rslt.append(b)
                            # print(b)
                        i += 1
                        item = {}

                except Exception as e:
                    # print(e)
                    pass

        return rslt
