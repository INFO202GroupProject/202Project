import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

df=pd.read_csv('beer_database_final.csv', encoding='ISO-8859-1')

def newDict(string):
    dict_list = {num: fuzz.partial_ratio(x.lower(), string) for num, x in enumerate(df['Beer_Name'])}

    t = sorted(dict_list.items(), key=lambda x:-x[1])[:100]

    new_dict = {}
    y=False
    for index, x in enumerate(t,1):
        if index==1 and x[1] != 100:
            y = True
        if x[1] == 100:
            new_dict[index] = [df.ix[x[0], 'Beer_Name'], x[0]]
        if y and x[1] > 80:
            new_dict[index] = [df.ix[x[0], 'Beer_Name'], x[0]]
    return new_dict

def beerSearch(string):

    new_dict = newDict(string)

    final_list = []
    for key, value in new_dict.items():
        final_list.append(str(key)+" : "+str(value[0]))
    return print('\n'.join(final_list))

def genericBeerInfo(num, string):
    new_dict = newDict(string)

    df1 = df.ix[new_dict[num][1],['Beer_Name', 'Beer_Description', 'styleName','abvClass','beerColor','breweryName','locality']]
    
    column_list = ['Name', 'Description', 'Style','ABV classification','Color','Brewery','Location of brewery']
    
    final_list = []
    for i, value in enumerate(df1):
        if pd.isnull(value):
            continue
        else: 
            final_list.append(str(column_list[i])+': '+str(value)+'\n')
    return print('\n'.join(final_list))

def getOccasion(num, string):
    new_dict = newDict(string)

    df1 = df.ix[new_dict[num][1],['Occassion']]
    
    column_list = ['Occassion']
    
    final_list = []
    for i, value in enumerate(df1):
        if pd.isnull(value):
            final_list.append(str(column_list[i])+': sorry the occassion information is not available\n')
        else: 
            final_list.append(str(column_list[i])+': '+str(value)+'\n')
    return print('\n'.join(final_list))

def getFoodPairing(num, string):
    new_dict = newDict(string)

    df1 = df.ix[new_dict[num][1],['foodPairings','Ingredients','Dishes','IngredientsDishes']]
    
    column_list = ['foodPairings','Ingredients','Dishes','IngredientsDishes']
    
    final_list = []
    for i, value in enumerate(df1):
        if pd.isnull(value):
            continue
            #final_list.append(str(column_list[num])+': sorry the occassion information is not available\n')
        else: 
            final_list.append(str(column_list[i])+': '+str(value)+'\n')
    return print('\n'.join(final_list))

def runBeerSearch():
    while True:
        text=str(input("What beer would you like to search for?: ")).lower() #Prompt user for query in seach engine
        
        new_dict = newDict(text)

        if len(new_dict) < 1:
            print ('Sorry we do not have any beers that match your search.')

            finalSelection = input("Would you like to search for another beer? Y/N\n").lower()
            if finalSelection == 'n':
                break

        else:
            beerSearch(text)

            selection = int(input("Select the number for more information on the respective beer: "))

            genericBeerInfo(selection, text)

            nextSelection = int(input("What other information would you like to know? \n1: Occasion information\n2: Food pairing information \n3: End\nEnter numeric value: "))

            df1 = df.ix[new_dict[selection][1],['Beer_Name']]
            if nextSelection == 1:
                print('Name: '+str(df1[0])+'\n')
                getOccasion(selection, text)
            elif nextSelection == 2:
                print('Name: '+str(df1[0])+'\n')
                getFoodPairing(selection, text)
            else:
                break

            finalSelection = input("Would you like to search for another beer? Y/N\n").lower()
            if finalSelection == 'n':
                break
