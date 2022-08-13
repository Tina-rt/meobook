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
meobook = Meobook()
#List of 5 books fetch from google
list_of_book = meobook.search_book("git hub cheat sheet")

#Download one book
book1 = list_of_book.download("/your/destination/path")
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