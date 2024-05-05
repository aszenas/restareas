"""
Name:    Anna Szenas
CS230:   CS230-5
Data:    Rest Areas In California
URL:

Description:

This program creates the Intro page of the Streamlit webpage, describing the Rest Areas In California.
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

#homepage title:
st.title("Exploring Rest Areas in California")

#description:
'''
Rest areas are vital for travelers, offering a safe place to rest, stretch, and recharge during long journeys. 
The following pages provide valuable insights into these crucial facilities, helping travelers make informed 
decisions about their stops across the state of California.
'''

#image:
#[ST4]:
from PIL import Image
rest_img = Image.open("C:/Users/Felhasználó/Desktop/Annaa/corvinus/6. semester bentley/intro to python/codes/pythonProject/final_project/rest_area_image.jpg")
st.image(rest_img,width=700)

#[ST4]:
#I also have different pages in the pages folder, which the user can access through the sidebar



