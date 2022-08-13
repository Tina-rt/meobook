from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent

VERSION = '0.0.7' 
DESCRIPTION = 'Module to search and download a book from the internet'
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="MeoBook", 
        version=VERSION,
        author="Tina Ratolojanahary",
        author_email="<rtinahubert@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        packages=find_packages(),

        install_requires=['bs4', 'requests'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        url="https://github.com/Tina-rt/meobook",
        
        keywords=['python', 'download book', 'pdf downloader', 'book search engine'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)