# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 15:42:57 2018
EX 1
@author: Anil
"""

import pandas as pd
from nltk.tokenize import sent_tokenize
from nltk.chunk import ne_chunk
import csv

def read_File():
    df = pd.read_csv("C:\\Users\\Renu\\Desktop\\TopGear AI & ML basics\\dara_in.csv", delimiter=',', error_bad_lines=False,  encoding='utf-8')
    return df

if __name__ == '__main__':
    myCsv = read_File()
    sentences=[]
    my_sentences=[]
    i=0
    j=0
    hi = '''"']''';
    hello = '''['"''';
    myList = myCsv.values.tolist()
    for i in range(len(myList)):
        my_whole_sentence = str(myList[i]).replace(hi,"").replace(hello,"")
        my_sentences = sent_tokenize(my_whole_sentence)
        for j in range(len(my_sentences)):
            sentences.append(my_sentences[j])
    print(sentences)
    
    #Assuming a list into a file
    csvfile = "C:\\Users\\Renu\\Desktop\\TopGear AI & ML basics\\dara_out.csv"
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for my_row in sentences:
            writer.writerow([my_row])    
    
    chunk_sentence = ne_chunk(sentences)
    print(chunk_sentence)    
            