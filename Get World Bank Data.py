# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:53:01 2021

@author: User
"""

import wbdata
import pandas as pd

###Targeted resources:
#https://data.worldbank.org/indicator/NY.GDP.COAL.RT.ZS?locations=ZA
#>> https://data.worldbank.org/indicator/```Indicators```?locations=```country```

#Set up countries
countries = ["ZA", "CN"]

#Set up indicators (by dictionary)
indicators = {"NY.GDP.COAL.RT.ZS":"Coal Rent"} #Assign and name the indicators

#Get data
df = wbdata.get_dataframe(indicators, country = countries)

#Unstack dataframe
df_new = df.unstack(level = 0)