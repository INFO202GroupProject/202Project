import sys
sys.path.insert(0, '/anaconda/lib/python3.6/site-packages')
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from itertools import chain
from nltk.corpus import stopwords
import json

df=pd.read_csv('beer_database_final.csv', encoding='ISO-8859-1')

Description_list=list(df.foodPairings)

Description_list=[str(i) for i in Description_list] #change descriptions to string format to allow for word tokenization

def makeInvertedIndex(strlist):
    """Function to make an inverted index; a dictionary where each key is a word in our foodpairing vocabulary, \
    and corresponding values are indexes of different beers that conatin the vocabulary word"""
    words=set(chain(*[word_tokenize(i.lower()) for i in strlist])) #create vocabulary of foodpairing words by tokenizing
    inverteddict={i:{idx for idx, val in enumerate(strlist) if i in val.split()} for i in words} #create dictionary with key as vocabulary word and values as idex of beers that contain vocabulary word
    inverteddict=dict(inverteddict)
    return inverteddict
    

   
def andSearch(invertedIndex, query):
    """Function that retrieves indexes of beers that contain any of the words in the user's query"""    
    value=[invertedIndex.get(i.lower()) for i in query]
    if None in value:
        return print ("We are sorry, we couldn't find any beers that match your query at this time. Please come back later. We'll keep working to get beers that match your search.")
    indexes=[invertedIndex[i.lower()] for i in query] #loop through words in user's query and find inverted index values corresponding to the words
    indexes=set.intersection(*indexes) #make individual sets of indexes one larger set
    if len(indexes)>0:
        return indexes
    else:
        return print ("We are sorry, we couldn't find any beers that match your query at this time. Please come back later. We'll keep working to get beers that match your search.")

def SearchResults(setvalues):
    df=pd.read_csv('beer_database_final.csv', encoding='ISO-8859-1')
    """Function makes a new dataframe containing"""
    df1=df.loc[list(setvalues),['Beer_Name','styleName','ABV']]
    return df1
    
    
def printresults(df): 
    df1=df.transpose()
    df1.columns=['']*len(df1.columns)
    pd.set_option('display.max_colwidth', -1)
    final_list = []
    for key, value in df1.items():
        final_list.append(str(key)+str(value))
    return print('\n'.join(final_list))
    
    
    


#with open('InvertedIndex.txt', 'w') as outfile:
    #json.dump(OurInvertedIndex, outfile)
    
OurInvertedIndex=makeInvertedIndex(Description_list) 
    
def RunPairingSearch():
    attempts=3
    while attempts>0:
        text=str(input("What are you thinking about having with your beer?: ")) #Prompt user for query in seach engine

        if len(text) < 1:
            print ('Sorry we do not have any beers that match your search.')
            finalSelection = input("Would you like to search for another beer? Y/N\n").lower()
            if finalSelection == 'n':
                break
        
        else:
            word_list=text.split()
            filtered_words = [word for word in word_list if word not in stopwords.words('english')]
            andSearchResults=andSearch(OurInvertedIndex, filtered_words)
            if andSearchResults is not None:
                b=SearchResults(andSearchResults)
                printresults(b)
            else:
                attempts-=1
                continue
            finalSelection = input("Would you like to search for another kind of food? Y/N\n").lower()
            if finalSelection == 'n':
                break   
                
                
            