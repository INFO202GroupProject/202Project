import pandas as pd
import numpy as np
from searchBeer import *
#from InvertedIndexFoodsearch import *
from locationSearch import *

while True:
	user_input = int(input("How would you like to search for a particular beer?\n[1] By name\n[2] By location\n[3] By food pairing\nEnter numeric value:"))

	if user_input == 1:
		runBeerSearch()
		break
	if user_input == 2:
		searchBreweriesNearby()
		break
	#if user_input == 3:
		#Ayo to add code
		#break
	else:
		selection = input ("Error. Would you like to retry your search? [y/n]").lower()
		if selection == 'n':
			break
		else:
			continue
