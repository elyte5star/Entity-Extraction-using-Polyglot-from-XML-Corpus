# XML_Parser
 Entity extraction with polyglot.
 
I am using Anaconda prompt.

I am Using windows.

#==============================#
#Important Libraries to install#
#==============================#

pip install nltk

import nltk

nltk.download('punkt')

from nltk import word_tokenize

import xml.etree.ElementTree as ET   ##This is used because the corpus contain documents with xml file format.

Install Polyglot
#===============================#
Getting the polyglot to work is tricky that was why I attached a folder with the polyglot files.
Ensure that they are in the folder and it will run.
But you can donwload polyglot using: 
git clone https://github.com/aboSamoor/polyglot.git

import polyglot

from polyglot.text import Text

from polyglot.downloader import downloader

downloader.download("TASK:embeddings2")

downloader.download("TASK:ner2")

You will get a ModuleNotFoundError this is because The needed text Python script was inside of nested polyglot folders.
To skip this issue use the polyglot folder i attached.

For polyglot.text to work it has shared requirements which includes wheel, PyICU, pycld2, six, futures, morfessor, and numpy.

This link provides a perfect guide on how to install everything correctly:
https://medium.com/@tlachacml/a-guide-for-using-polyglot-on-windows-8cbd8f97c7b0

Solution
Download the binary files from : https://www.lfd.uci.edu/~gohlke/pythonlibs/

Select the correct PyICU and pycld2 scripts. Make sure the numbers after “cp” are the same as your version of Python, for instance since my version number was 3.7.6, I wanted a Windows binary with “cp37”. Additionally, make sure the ending of the Windows binary is “win32” if you have 32-bit Python program and “amd64” if you have a 64-bit Python program.
Click on the correct Window binaries for PyICU and pycld2. This will automatically download these packages saved in Wheel formats into your download folder.

Now u can use pip like this for example:

pip install C:\Users\check\<name of location of the binary file> PyICU-2.6-cp36-cp36m-win_amd64.whl

pip install C:\Users\check\<name of location of the binary file> pycld2-0.41-cp36-cp36m-win_amd64.whl

Next step

pip install morfessor
