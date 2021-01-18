# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 10:25:50 2021

@author: User
"""

import investpy
import pandas as pd
### API reosurce ###
#https://pypi.org/project/investpy/

################################################
############ Index Example ############
################################################
###### FTSE/JSE Coal Mining
#Check format of the country you want in this API
index_country = investpy.get_index_countries()

#Check available index name of the wanted country
available_index = investpy.get_indices('south africa')

#Get the data when correct country and variable name is confirmed
df = investpy.get_index_historical_data(index = "FTSE/JSE Coal Mining", 
                                        country = "south africa", 
                                        from_date = "10/01/2008",
                                        to_date = "01/01/2021")

#Get recent data (recent for 1 month) -- useful for short-term data retrieval
df_r = investpy.get_index_recent_data(index = "FTSE/JSE Coal Mining", 
                                        country = "south africa")

################################################
############ Futures Example ############
################################################
#When futures is set there is no need to define contry
#The key for searching approprriate commodity you want is "groups"

#Check what "groups" the API provide.
commodity_group_lst = investpy.get_commodity_groups()

###### NewC futures
#Search commodities
search_commodities = investpy.search_quotes(text = "Newcastle Coal Futures", 
                                            products = ['commodities'])
'''
for search in search_commodities:
    print(search)
'''

#Get data from search results
search_result = search_commodities.pop(0)
NewC_futures = search_result.retrieve_historical_data(from_date = "01/01/2009", 
                                                      to_date = "01/01/2021")



###### Coal (API4) FOB Richards Bay (ARGUS-McCloskey) Futures
search_richard_bay_future = investpy.search_quotes(text = "Coal (API4) FOB Richards Bay (ARGUS-McCloskey) Futures",
                                                   products = ["commodities"])

search_result_richard_bay = search_richard_bay_future.pop(0)
richard_bay_futures = search_result_richard_bay.retrieve_historical_data(from_date = "12/01/2012", 
                                                                         to_date = "18/01/2021")







