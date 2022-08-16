# MeoBook
A module to search and download a book from the internet

## Description
This is a package for searching a book and downloading it from the internet

## Installation
```bash
pip install meobook
```
## Usage
```Python
from MeoBook import MeoBook
meobook = MeoBook()
#the search method will return maximum of 5 books by default in a list of Book object 
list_of_book = meobook.search_book("git hub cheat sheet")

#Download one book
book1 = list_of_book[0].download("/your/destination/path")


#
```
## Docs
### Methods in MeoBook object
```python
self.search_book(keyword, limit=5)
```
```limit``` parameter limits the return results from ```self.search_book``` function

## Credits
Tina Hubert Ratolojanahary (rtinahubert@gmail.com, https://tina-rt.netlify.app)

Made in Madagascar
