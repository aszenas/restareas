"""
Name:    Anna Szenas
CS230:   CS230-5
Data:    Rest Areas In California
URL:

Description:

This program creates one page for the Streamlit webpage, describing the Rest Areas In California. On this page
users can choose a city from the menu and the webpage displays all the rest aras near their chosen city.
"""

import pandas as pd
import streamlit as st

#my path:
path = "C:/Users/Felhasználó/Desktop/Annaa/corvinus/6. semester bentley/intro to python/codes/pythonProject/final_project/"

st.set_option('deprecation.showPyplotGlobalUse', False)

#reading the dataframe:
rest_areas = pd.read_csv(path + "Rest_Areas.csv")

#[DA1]:
rest_areas.dropna(inplace=True)
rest_areas.rename(columns={"LATITUDE":"lat", "LONGITUDE": "lon"}, inplace= True)

#page title:
st.title("Exploring Rest Areas in California: Rest areas Near Cities")

#description:
'''
Page Summary:
'''
'''
This page enables you to discover rest areas close to specific cities in California. Simply select a city from the
drop-down menu, and the rest areas near your chosen city will be displayed.
'''

#citylist:
citylist = []

#[DA8]:
for index, row in rest_areas.iterrows():
    city = row["CITY"]
    traffic_direction = row["TRAFFICDIR"]

    #if city is not in the list, then append
    if city not in citylist:
        citylist.append(city)

#creating selection:
citylist.append("A selection needs to be made:")
#[PY1]:
citylist = sorted(citylist, reverse = False)
del citylist[0]

#[ST3+]:
select_city = st.selectbox("Select a city:", citylist)

#creating empty list for the matching areas
matching_rest_areas = []

#finding matching areas
#[DA8]:
for index, row in rest_areas.iterrows():
    city = row["CITY"]
    rest_area_name = row["NAME"]

    #check if the city and trafficdir matches the selected ones
    if city == select_city:
        matching_rest_areas.append(rest_area_name)

#displaying matching areas
if matching_rest_areas != []:
    st.write(f"Rest areas near the city {select_city}:")
    for area in matching_rest_areas:
        st.write(area)
else:
    st.write("You haven't made a selection yet.")

