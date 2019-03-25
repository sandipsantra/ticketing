import xlrd
import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

def text_processing(text):
    filtered_sent=[]
    ps = PorterStemmer()
    stop_words=set(stopwords.words("english"))
    raw_data=text
    try:
        preprocess=re.findall(r"Subject:(.*)[\n]*([\w\W\s\S\d\D]*)",raw_data)
        special_character_remove=preprocess[0][2]
    except:
        try:
            preprocess=re.findall(r"call_back_number:(.*)[\n]*([\w\W\s\S\d\D]*)",raw_data)
            special_character_remove=preprocess[0][1]               
        except:
            try:
                preprocess=re.findall(r"Location:(.*)[\n]*([\w\W\s\S\d\D]*)",raw_data)
                special_character_remove=preprocess[0][1] 
            except:
                try:
                    preprocess=re.findall(r"issue type|Issue Type:(.*)[\n]*([\w\W\s\S\d\D]*)",raw_data)
                    special_character_remove=preprocess[0][1]
                except:
                    special_character_remove=raw_data
    #clean_text.append(special_character_remove)
    des_data=special_character_remove
    lower_case=des_data.lower()
    tokenized_word=word_tokenize(lower_case)
    for w in tokenized_word:
        if w not in stop_words:
            reg=re.compile('[^\w\s]')
            if(reg.search(w)==None):
                w1=ps.stem(w)
                filtered_sent.append(w1)
            else:
                pass
                                
    temp=' '.join(filtered_sent)
    return temp
