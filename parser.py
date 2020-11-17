import os
import re
import tarfile
import polyglot
from polyglot.text import Text
from polyglot.downloader import downloader
downloader.download("TASK:embeddings2")
downloader.download("TASK:ner2")
import xml.etree.ElementTree as ET
import nltk
nltk.download('punkt')
from nltk import word_tokenize
from collections import Counter

#==============================================================#
#Unzips the archives and extracts all the text in each xml file#
#==============================================================#
class MyParser:
    def __init__(self,file=None):
        cwd = os.getcwd()
        self.my_string = None
        if file is not None:
            self.file = file
            try:
                f = tarfile.open(cwd + '/' + self.file,'r')
                f.extractall() #Extract all file to the current working directory.
                names = f.getnames()
                corpus = []
                for name in names:
                    if (name).endswith("xml") is True:
                        tree = ET.parse(cwd + '/'+ name)
                        txt = ET.tostringlist(tree.getroot(), encoding='utf-8', method='text')
                        corpus.extend(txt)
                self.my_string = str(corpus).strip('[]')
            except:
                print('cannot open', self.file)
#=============================================================================================================#
#Locations (Tag: I-LOC): cities, countries, regions, continents, neighborhoods, administrative divisions …    #
#Organizations (Tag: I-ORG): sports teams, newspapers, banks, universities, schools, non-profits, companies, …#
#Persons (Tag: I-PER): politicians, scientists, artists, atheletes …                                          #
#https://polyglot.readthedocs.io/en/latest/NamedEntityRecognition.html                                        #
#=============================================================================================================#
    def __call__(self):
        url = re.compile(r'https?://\S+|www\.\S+') #remove Links
        self.my_string = url.sub(r'',self.my_string,re.IGNORECASE)
        result = ''.join([i for i in self.my_string if not i.isdigit()]) 
        special_xter = re.compile(r'[^A-Za-z0-9]+') #remove special xters
        text = special_xter.sub(r' ',result) 
        text = ''.join([i.lower() for i in text if not i.isdigit()]) 
        text = word_tokenize(text)
        text =[i for i in text if i!= 'n']
        text = ' '.join(text)
        self.my_string = Text(text)
        Tags = [x.tag for x in self.my_string.entities]
        #print(self.my_string.entities) ##Prints all entities
        #dict_mapping = Counter(Tags)
        #print(dict_mapping) #optional Dictionary format
        return  dict([[x,Tags.count(x)] for x in set(Tags)]) #returns count for the entity categories
        
        
aux = MyParser("06.tgz")
print(aux())
#                       Output
#=========================================================#
#Counter({'I-PER': 97957, 'I-LOC': 43062, 'I-ORG': 21348})#
#[['I-PER', 97957], ['I-LOC', 43062], ['I-ORG', 21348]]   #
#======================================================== #