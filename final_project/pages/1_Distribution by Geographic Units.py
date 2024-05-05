"""
Name:    Anna Szenas
CS230:   CS230-5
Data:    Rest Areas In California
URL:

Description:

This program creates one page for the Streamlit webpage, describing the Rest Areas In California. On this page
users can explore the distribution of rest areas in california across geographic units such as districts, counties
or routes. The distribution is represented on a barchart and the webpage also displays the maximum and minimum values
with the corresponding geographical units. Additionally, users can check the data table, by using a checkbox.
"""

import pandas as pd
import matplotlib.pyplot as plt
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
st.title("Exploring Rest Areas in California: Analyzing Rest Area Distribution by Geographic Units")

#description:
'''
Page Summary:
'''
'''
This page allows you to visualize the distribution of rest areas in California across different geographic units. 
Choose one or more options from routes, districts, or counties to see the number of rest areas represented on a 
bar chart. By examining these charts, you can gain insights into the distribution of rest areas across specific 
geographic units, helping you plan your travels in California more effectively and understand where rest areas are 
concentrated.
'''

#multiselect for the bars:
#[ST1]:
selection = ["Districts","Counties","Routes"]
selected = st.multiselect("I want to see the number of Rest Areas by: ", selection)

#if nothing is selected:
if len(selected) == 0:
    st.write("You haven't made a selection yet")

#bar1 - [VIZ1]
if "Districts" in selected:
    #[DA7]:
    df_bar1D = rest_areas["DISTRICT"].value_counts()  #get a series
    #[DA2]:
    df_bar1D = df_bar1D.sort_values(ascending=False) #sort descending
    df_bar1D.plot(kind="bar", color="red") #plot the bar chart
    plt.title("Number of Rest Areas in each District") #chart title
    plt.ylabel("Number of Rest Areas") #y axis label
    plt.xlabel("Districts") #x axis label
    st.pyplot()

    #[DA3]:
    #getting the min max value
    min_areas_d = df_bar1D.min()
    max_areas_d = df_bar1D.max()

    #getting the districts with the max and min values:
    #[PY5]: Creating the dictionary - I will document accessing its values with "[PY5]-A"
    minmax_district_dict = {"min":[],
                            "max":[]}
    for index, count in df_bar1D.items():
        if count == min_areas_d:
            minmax_district_dict["min"].append(index)
        if count == max_areas_d:
            minmax_district_dict["max"].append(index)

    #displaying districts:
    #[PY4]: (+[PY5]-A)
    display_maxd = [str(i) for i in minmax_district_dict["max"]]
    display_maxd_str = ", ".join(display_maxd)
    st.write(f"The district(s) with the maximum amount of rest areas is/are: {display_maxd_str} - with the number of {max_areas_d} rest areas.")

    # [PY4]: (+[PY5]-A)
    display_mind = [str(i) for i in minmax_district_dict["min"]]
    display_mind_str = ", ".join(display_mind)
    st.write(f"The district(s) with the minimum amount of rest areas is/are: {display_mind_str} - with the number of {min_areas_d} rest areas.")

    #checkbox for the table
    #[ST3]:
    show_table1 = st.checkbox("Check if you want to see the table for the 'Number of rest areas in each District'")
    if show_table1:
        st.write(df_bar1D)

#bar2 - [VIZ1]
if "Counties" in selected:
    # [DA7]:
    df_bar1C = rest_areas["COUNTY"].value_counts() #get a series
    # [DA2]:
    df_bar1C = df_bar1C.sort_values(ascending=False) #sort descending
    df_bar1C.plot(kind="bar", color="red") #plot the bar chart
    plt.title("Number of Rest Areas in each County") #chart title
    plt.ylabel("Number of Rest Areas") #y axis label
    plt.xlabel("Counties") #x axis label
    st.pyplot()

    # [DA3]:
    #getting the min max value
    min_areas_c = df_bar1C.min()
    max_areas_c = df_bar1C.max()

    # getting the counties with the max and min values:
    # [PY5]: Creating the dictionary - I will document accessing its values with "[PY5]-A"
    minmax_counties_dict = {"min": [],
                            "max": []}
    for index, count in df_bar1C.items():
        if count == min_areas_c:
            minmax_counties_dict["min"].append(index)
        if count == max_areas_c:
            minmax_counties_dict["max"].append(index)

    # displaying dcounties:
    # [PY4]: (+[PY5]-A)
    display_maxc = [str(i) for i in minmax_counties_dict["max"]]
    display_maxc_str = ", ".join(display_maxc)
    st.write(f"The county/counties with the maximum amount of rest areas is/are: {display_maxc_str} - with the number of {max_areas_c} rest areas.")

    # [PY4]: (+[PY5]-A)
    display_minc = [str(i) for i in minmax_counties_dict["min"]]
    display_minc_str = ", ".join(display_minc)
    st.write(f"The county/counties with the minimum amount of rest areas is/are: {display_minc_str} - with the number of {min_areas_c} rest area.")

    # checkbox for the table
    # [ST3]:
    show_table2 = st.checkbox("Check if you want to see the table for the 'Number of rest areas in each County'")
    if show_table2:
        st.write(df_bar1C)

#bar3 - [VIZ1]
if "Routes" in selected:
    # [DA7]:
    df_bar1R = rest_areas["ROUTE"].value_counts() #get a series
    # [DA2]:
    df_bar1R = df_bar1R.sort_values(ascending = False) #sort descending
    df_bar1R.plot(kind = "bar", color = "red") #plot the bar chart
    plt.title("Number of Rest Areas along each Route") #chart title
    plt.ylabel("Number of Rest Areas") #y axis label
    plt.xlabel("Routes") #x axis label
    st.pyplot()

    # [DA3]:
    min_areas_r = df_bar1R.min()
    max_areas_r = df_bar1R.max()

    # getting the routes with the max and min values:
    # [PY5]: Creating the dictionary - I will document accessing its values with "[PY5]-A"
    minmax_routes_dict = {"min": [],
                          "max": []}
    for index, count in df_bar1R.items():
        if count == min_areas_r:
            minmax_routes_dict["min"].append(index)
        if count == max_areas_r:
            minmax_routes_dict["max"].append(index)

    # displaying routes:
    # [PY4]: (+[PY5]-A)
    display_maxr = [str(i) for i in minmax_routes_dict["max"]]
    display_maxr_str = ", ".join(display_maxr)
    st.write(f"The route(s) with the maximum amount of rest areas is/are: {display_maxr_str} - with the number of {max_areas_r} rest areas.")

    # [PY4]: (+[PY5]-A)
    display_minr = [str(i) for i in minmax_routes_dict["min"]]
    display_minr_str = ", ".join(display_minr)
    st.write(f"The route(s) with the minimum amount of rest areas is/are: {display_minr_str} - with the number of {min_areas_r} rest area.")

    # checkbox for the table
    # [ST3]:
    show_table3 = st.checkbox("Check if you want to see the table for the 'Number of Rest Areas along each Route'")
    if show_table3:
        st.write(df_bar1R)

#checkbox: https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox

#counting how many times something occours in a column:
#https://saturncloud.io/blog/what-is-the-most-efficient-way-of-counting-occurrences-in-pandas/
    #When I first tried to count all the rest areas in each district, I tried to do it with groupby and it did not work very well.
    #Then I found this ".value_counts()" method and by using this I was able to get a serie of the "counts", which I found very useful.