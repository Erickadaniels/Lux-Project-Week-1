#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

doc = pd.read_csv('/home/dishon/Downloads/ASSIGNMENT/1. Weather Data.csv')
print('Weather Data Length: {}'.format(len(doc)))
print(doc.head(10))
print(doc.tail(10))
# 1. Find all records where the weather was exactly clear.
clear_weather_records = doc[doc['Weather'] == 'Clear']
print(clear_weather_records)

# 2. Find the number of times the wind speed was exactly 4 km/hr.
wind_speed_4_count = len(doc[doc['Wind Speed_km/h'] == 4])
print(f"Number of times the wind speed was exactly 4 km/hr: {wind_speed_4_count}")

# 3. Check if there are any NULL values present in the dataset.
null_values = doc.isnull().sum()
print(f"NULL values in the dataset: {null_values}")

# 4. Rename the column "Weather" to "Weather_Condition."
doc.rename(columns={'Weather': 'Weather_Condition'}, inplace=True)
print(doc.head())

# 5. What is the mean visibility of the dataset?
mean_visibility = doc['Visibility_km'].mean()
print(f"Mean visibility of the dataset: {mean_visibility}")

# 6. Find the number of records where the wind speed is greater than 24 km/hr and visibility is equal to 25 km.
specific_records_count = len(doc[(doc['Wind Speed_km/h'] > 24) & (doc['Visibility_km'] == 25)])
print(f"Number of records where the wind speed is greater than 24 km/hr and visibility is equal to 25 km: {specific_records_count}")

# 7. What is the mean value of each column for each weather condition?
mean_values_by_weather = doc.groupby('Weather_Condition').mean()
print(mean_values_by_weather)

# 8. Find all instances where the weather is clear and the relative humidity is greater than 50, or visibility is above 40.
specific_conditions = doc[(doc['Weather_Condition'] == 'Clear') & 
                                   ((doc['Rel Hum_%'] > 50) | (doc['Visibility_km'] > 40))]
print(specific_conditions)

# 9. Find the number of weather conditions that include snow.
snow_conditions_count = len(doc[doc['Weather_Condition'].str.contains('Snow', case=False, na=False)])
print(f"Number of weather conditions that include snow: {snow_conditions_count}")
