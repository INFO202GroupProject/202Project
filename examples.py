#Download the brewerydb.py file from here ->> https://github.com/yarian/brewerydb
from brewerydb import * 

#Replace param with your api key
BreweryDb.configure("YOUR_API_KEY")

###############Example API Calls################################
#Uncomment the print() statements to test/see output of each call


#Style - get a particular style
##Param: style id
##Return: style object (contains 'id', 'name', 'shortName', 'description')
#print(BreweryDb.style('2'))

#Styles - get all styles
##Param: none
##Returns: style objects in 'data' attribute
#print(BreweryDb.styles())

#Category
##Param: category id
##Return: category obj (contains 'id', 'name')
#print(BreweryDb.category('3'))

#Categories - get all categories
##Param: none
##Return: category objects in 'data' attribute
#print(BreweryDb.categories())

#Features 
##Param: none
#Return: featured beers
#print(BreweryDb.features())

#Search
##Param: {"type":  , "q":  } 
##Return: (depends on the type and q(query), example returns beers with "British in name")
#print(BreweryDb.search({"type":"beer", "q": "british"}))

#Beers with Stout in the name
#BreweryDb.beers({'name': 'Stout'})


#For convenience, these are the category, style and ingredient names
categories = ['British Origin Ales', 'Irish Origin Ales', 'North American Origin Ales', 'German Origin Ales', 'Belgian And French Origin Ales', 'International Ale Styles', 'European-germanic Lager', 'North American Lager', 'Other Lager', 'International Styles', 'Hybrid/mixed Beer', 'Mead, Cider, & Perry', 'Other Origin', 'Malternative Beverages', '""']
styles = ['Classic English-Style Pale Ale', 'English-Style India Pale Ale', 'Ordinary Bitter', 'Special Bitter or Best Bitter', 'Extra Special Bitter', 'English-Style Summer Ale', 'Scottish-Style Light Ale', 'Scottish-Style Heavy Ale', 'Scottish-Style Export Ale', 'English-Style Pale Mild Ale', 'English-Style Dark Mild Ale', 'English-Style Brown Ale', 'Old Ale', 'Strong Ale', 'Scotch Ale', 'British-Style Imperial Stout', 'British-Style Barley Wine Ale', 'Brown Porter', 'Robust Porter', 'Sweet or Cream Stout', 'Oatmeal Stout', 'Irish-Style Red Ale', 'Classic Irish-Style Dry Stout', 'Foreign (Export)-Style Stout', 'American-Style Pale Ale', 'Fresh "Wet" Hop Ale', 'Pale American-Belgo-Style Ale', 'Dark American-Belgo-Style Ale', 'American-Style Strong Pale Ale', 'American-Style India Pale Ale', 'Imperial or Double India Pale Ale', 'American-Style Amber/Red Ale', 'Imperial Red Ale', 'American-Style Barley Wine Ale', 'American-Style Wheat Wine Ale', 'Golden or Blonde Ale', 'American-Style Brown Ale', 'Smoke Porter', 'Brett Beer', 'American-Style Sour Ale', 'American-Style Black Ale', 'American-Style Stout', 'American-Style Imperial Stout', 'Specialty Stouts', 'German-Style Kölsch / Köln-Style Kölsch', 'Berliner-Style Weisse (Wheat)', 'Leipzig-Style Gose', 'South German-Style Hefeweizen / Hefeweissbier', 'South German-Style Kristall Weizen / Kristall Weissbier', 'German-Style Leichtes Weizen / Weissbier', 'South German-Style Bernsteinfarbenes Weizen / Weissbier', 'South German-Style Dunkel Weizen / Dunkel Weissbier', 'South German-Style Weizenbock / Weissbock', 'Bamberg-Style Weiss (Smoke) Rauchbier (Dunkel or Helles)', 'German-Style Altbier', 'Kellerbier (Cellar beer) or Zwickelbier - Ale', 'Belgian-Style Flanders Oud Bruin or Oud Red Ales', 'Belgian-Style Dubbel', 'Belgian-Style Tripel', 'Belgian-Style Quadrupel', 'Belgian-Style Blonde Ale', 'Belgian-Style Pale Ale', 'Belgian-Style Pale Strong Ale', 'Belgian-Style Dark Strong Ale', 'Belgian-Style White (or Wit) / Belgian-Style Wheat', 'Belgian-Style Lambic', 'Belgian-Style Gueuze Lambic', 'Belgian-Style Fruit Lambic', 'Belgian-Style Table Beer', 'Other Belgian-Style Ales', 'French-Style Bière de Garde', 'French & Belgian-Style Saison', 'International-Style Pale Ale', 'Australian-Style Pale Ale', 'German-Style Pilsener', 'Bohemian-Style Pilsener', 'German-Style Leichtbier', 'Münchner (Munich)-Style Helles', 'Dortmunder / European-Style Export', 'Vienna-Style Lager', 'German-Style Märzen', 'German-Style Oktoberfest / Wiesen (Meadow)', 'European-Style Dark / Münchner Dunkel', 'German-Style Schwarzbier', 'Bamberg-Style Märzen Rauchbier', 'Bamberg-Style Helles Rauchbier', 'Bamberg-Style Bock Rauchbier', 'Traditional German-Style Bock', 'German-Style Heller Bock/Maibock', 'German-Style Doppelbock', 'German-Style Eisbock', 'Kellerbier (Cellar beer) or Zwickelbier - Lager', 'American-Style Lager', 'American-Style Light (Low Calorie) Lager', 'American-Style Low-Carbohydrate Light Lager', 'American-Style Amber (Low Calorie) Lager', 'American-Style Premium Lager', 'American-Style Pilsener', 'American-Style Ice Lager', 'American-Style Malt Liquor', 'American-Style Amber Lager', 'American-Style Märzen / Oktoberfest', 'American-Style Dark Lager', 'Baltic-Style Porter', 'Australasian, Latin American or Tropical-Style Light Lager', 'International-Style Pilsener', 'Dry Lager', 'Session Beer', 'American-Style Cream Ale or Lager', 'California Common Beer', 'Ginjo Beer or Sake-Yeast Beer', 'Light American Wheat Ale or Lager with Yeast', 'Light American Wheat Ale or Lager without Yeast', 'Fruit Wheat Ale or Lager with or without Yeast', 'Dark American Wheat Ale or Lager with Yeast', 'Dark American Wheat Ale or Lager without Yeast', 'Rye Ale or Lager with or without Yeast', 'German-Style Rye Ale (Roggenbier) with or without Yeast', 'Fruit Beer', 'Field Beer', 'Pumpkin Beer', 'Chocolate / Cocoa-Flavored Beer', 'Coffee-Flavored Beer', 'Herb and Spice Beer', 'Specialty Beer', 'Specialty Honey Lager or Ale', 'Gluten-Free Beer', 'Indigenous Beer (Lager or Ale)', 'Smoke Beer (Lager or Ale)', 'Experimental Beer (Lager or Ale)', 'Historical Beer', 'Wood- and Barrel-Aged Beer', 'Wood- and Barrel-Aged Pale to Amber Beer', 'Wood- and Barrel-Aged Dark Beer', 'Wood- and Barrel-Aged Strong Beer', 'Wood- and Barrel-Aged Sour Beer', 'Aged Beer (Ale or Lager)', 'Other Strong Ale or Lager', 'Non-Alcoholic (Beer) Malt Beverages', 'Dry Mead', 'Semi-Sweet Mead', 'Sweet Mead', 'Cyser (Apple Melomel)', 'Pyment (Grape Melomel)', 'Other Fruit Melomel', 'Metheglin', 'Braggot', 'Open Category Mead', 'Common Cider', 'English Cider', 'French Cider', 'Common Perry', 'Traditional Perry', 'New England Cider', 'Fruit Cider', 'Apple Wine', 'Other Specialty Cider or Perry', 'American-Style Imperial Porter', 'Adambier', 'Grodziskie', 'Flavored Malt Beverage', 'Energy Enhanced Malt Beverage', 'Double Red Ale', 'Session India Pale Ale', 'Contemporary Gose', 'Dutch-Style Kuit, Kuyt or Koyt', 'Belgian-style Fruit Beer', 'Chili Pepper Beer', 'Mixed Culture Brett Beer', 'Wild Beer']
ingredients = ['Admiral', 'Aged / Debittered Hops (Lambic)', 'Ahtanum', 'Amarillo', 'Amarillo Gold', 'Apollo', 'Aquila', 'Argentine Cascade', 'Aurora', 'Auscha (Saaz)', 'Goldings', 'Banner', 'Boadicea', 'Bobek', 'Bor', 'Bramling Cross', 'Bravo', "Brewer's Gold", 'Bullion', 'California Ivanhoe', 'Calypso', 'Cascade', 'Celeia', 'Centennial', 'Challenger', 'Chinook', 'Citra', 'Cluster', 'Columbia', 'Columbus', 'Columbus (Tomahawk)', 'Comet', 'Crystal', 'Czech Saaz', 'Delta', 'East Kent Goldings', 'El Dorado', 'Eroica', 'Experimental 946', "Falconer's Flight", 'First Gold', 'French Strisserspalt', 'Fuggles', 'Galaxy', 'Galena', 'German Magnum', 'German Opal', 'German Perle', 'German Select', 'German Tradition']
