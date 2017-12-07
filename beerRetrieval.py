import sys
sys.path.insert(0, '/anaconda/lib/python3.6/site-packages')

import pandas as pd
import numpy as np
from searchBeer import *
from InvertedIndexFoodsearch import *
from locationSearch import *


def mainPrompt():
	user_input = int(input("How would you like to search for a particular beer?\n[1] By name\n[2] By location\n[3] By food pairing\n[4] Quit \nEnter numeric value:"))

	while True:
		if user_input == 1:
			runBeerSearch()
			mainPrompt()
		if user_input == 2:
			searchBreweriesNearby()
			mainPrompt()
		if user_input == 3:
			RunPairingSearch()
			mainPrompt()
		if user_input == 4:
			print("Exiting...")
			sys.exit()
		else:
			selection = input ("Error. Would you like to retry your search? [y/n]").lower()
			if selection == 'n':
				break
			else:
				continue

mainPrompt()
