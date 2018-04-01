# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 15:42:57 2018
Ex 4
@author: Anil
"""

import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
#import csv

def read_File():
    df = pd.read_csv("C:\\Users\\Renu\\Desktop\\TopGear AI & ML basics\\NLPdataEx3&4-data_in.txt", delimiter=',', error_bad_lines=False,  encoding='utf-8')
    return df

if __name__ == '__main__':
    myCsv = read_File()
    sentences=[]
    my_sentences=[]
    words=[]
    pos_words=[]
    PS_words=[]
    Lem_words=[]
    i=0
    j=0
    m=0
    hi = '''"']''';
    hello = '''['"''';
    myList = myCsv.values.tolist()
    for i in range(len(myList)):
        my_whole_sentence = str(myList[i]).replace(hi,"").replace(hello,"")
        my_sentences = sent_tokenize(my_whole_sentence)
        for j in range(len(my_sentences)):
            sentences.append(my_sentences[j])
    print(sentences)
    
    
    for k in range(len(sentences)):
        my_splitup_of_words = word_tokenize(sentences[k])
        for l in range(len(my_splitup_of_words)):
            if my_splitup_of_words[l]=='[' or  my_splitup_of_words[l]==']' or  my_splitup_of_words[l]=='.' or  my_splitup_of_words[l]==',' or  my_splitup_of_words[l]=='?' or  my_splitup_of_words[l]=="'"  or  my_splitup_of_words[l]=='nan':
                continue
            words.append(my_splitup_of_words[l].replace("'",''))
    
    stop = set(stopwords.words('english'))
    
    ps = PorterStemmer()
    wnLemmat = WordNetLemmatizer()
    for m in range(len(words)):
        if words[m] not in stop:
           PS_words.append(ps.stem(words[m]))
           # Lemmatization throws belwo error
           #'AttributeError: 'WordNetLemmatizer' object has no attribute 'stem''
           #Lem_words.append(wnLemmat.stem(words[m]))
    
    print(PS_words)
    #print(Lem_words)
        
    
#    #Assuming a list into a file
#    csvfile = "C:\\Users\\Renu\\Desktop\\TopGear AI & ML basics\\dara_out.csv"
#    with open(csvfile, "w") as output:
#        writer = csv.writer(output, lineterminator='\n')
#        for my_words in words:
#            writer.writerow([my_words])    