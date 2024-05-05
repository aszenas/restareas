"""
Name:    Anna Szenas
CS230:   CS230-5
Data:    Rest Areas In California
URL:

Description:

This program creates one page for the Streamlit webpage, describing the Rest Areas In California. On this page
users can explore the percentages of rest areas with and without their chosen facilities. They can use tabs to
switch between the facilities they want to see, and every tab displays a pie chart with a checkbox, which can
show the data tables to the users.
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
st.title("Exploring Rest Areas in California: Percentage of Rest Areas with Selected Facilities")

#description:
'''
Page Summary:
'''
'''
On this page each tab displays a pie chart illustrating the percentage of rest areas with and without the chosen 
facility. By examining these pie charts, you can evaluate the availability of various amenities at rest areas across 
California. With this tool, you will also have a clearer understanding of what to expect when you stop at a rest area 
during your journey.
'''

#USING TABS FOR DIFFERENT KIND OF PIECHARTS:
#tabs: https://docs.streamlit.io/develop/api-reference/layout/st.tabs

tab_names = ["Restrooms","Water", "Picnic Tables","Phone","Vending Machines","Facilities for Handicapped Individuals","Station for Recreational Vehicles","Area designated for Pets"]

#[ST3+]:
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(tab_names)
#tab contents
with tab1:
    #[VIZ2]
   st.title("Percentage of Rest Areas with Restrooms") #title
    # [DA7]:
   pie_df1 = rest_areas["RESTROOM"].value_counts() #get the series
    # [DA2]:
   pie_df1.sort_index(inplace=True) #sort by index
   pielabels1 = ["With Restrooms"] #label
   piecolors1 = ["green"] #color
   pie_df1.plot(kind = "pie", colors = piecolors1, autopct = "%.1f%%", labels = pielabels1) #piechart
   plt.ylabel(" ") #removed the label "count" from the y axis
   st.pyplot()
   #checkbox for the table
   # [ST3]:
   showtable1 = st.checkbox("Check if you want to see the table for 'Percentage of Rest Areas with Restrooms'")
   if showtable1:
       st.write(pie_df1)

with tab2:
    # [VIZ2]
    st.title("Percentage of Rest Areas with Water") #title
    # [DA7]:
    pie_df2 = rest_areas["WATER"].value_counts() #get the series
    # [DA2]:
    pie_df2.sort_index(inplace=True) #sort by index
    pielabels2 = ["With Water"] #label
    piecolors2 = ["green"] #color
    pie_df2.plot(kind="pie", colors=piecolors2, autopct="%.1f%%", labels=pielabels2) #piechart
    plt.ylabel(" ") #removed the label "count" from the y axis
    st.pyplot()
    # checkbox for the table
    # [ST3]:
    showtable2 = st.checkbox("Check if you want to see the table for 'Percentage of Rest Areas with Water'")
    if showtable2:
        st.write(pie_df2)

with tab3:
    # [VIZ2]
    st.title("Percentage of Rest Areas with Picnic Tables") #title
    # [DA7]:
    pie_df3 = rest_areas["PICNICTAB"].value_counts() #get the series
    # [DA2]:
    pie_df3.sort_index(inplace=True) #sort by index
    pielabels3 = ["No Data","With Picnic Tables"] #label
    piecolors3 = ["blue","green"] #color
    pie_df3.plot(kind="pie", colors=piecolors3, autopct="%.1f%%", labels=pielabels3) #piechart
    plt.ylabel(" ") #removed the label "count" from the y axis
    st.pyplot()
    # checkbox for the table
    # [ST3]:
    showtable3 = st.checkbox("Check if you want to see the table for 'Percentage of Rest Areas with Picnic Tables'")
    if showtable3:
        st.write(pie_df3)

with tab4:
    # [VIZ2]
    st.title("Percentage of Rest Areas with Phone") #title
    # [DA7]:
    pie_df4 = rest_areas["PHONE"].value_counts() #get the series
    # [DA2]:
    pie_df4.sort_index(inplace=True) #sort by index
    pielabels4 = ["No Data", "Without Phone","With Phone"] #label
    piecolors4 = ["blue", "red", "green"] #color
    pie_df4.plot(kind="pie", colors=piecolors4, autopct="%.1f%%", labels=pielabels4) #piechart
    plt.ylabel(" ") #removed the label "count" from the y axis
    st.pyplot()
    # checkbox for the table
    # [ST3]:
    showtable4 = st.checkbox("Check if you want to see the table for 'Percentage of Rest Areas with Phone'")
    if showtable4:
        st.write(pie_df4)

with tab5:
    # [VIZ2]
    st.title("Percentage of Rest Areas with Vending Machines") #title
    # [DA7]:
    pie_df5 = rest_areas["VENDING"].value_counts() #get the series
    # [DA2]:
    pie_df5.sort_index(inplace=True) #sort by index
    pielabels5 = ["Without Vending Machines", "With Vending Machines"] #label
    piecolors5 = ["red","green"] #color
    pie_df5.plot(kind="pie", colors=piecolors5, autopct="%.1f%%", labels=pielabels5) #piechart
    plt.ylabel(" ") #removed the label "count" from the y axis
    st.pyplot()
    # checkbox for the table
    # [ST3]:
    showtable5 = st.checkbox("Check if you want to see the table for 'Percentage of Rest Areas with Vending Machines'")
    if showtable5:
        st.write(pie_df5)

with tab6:
    # [VIZ2]
    st.title("Percentage of Rest Areas with Facilities for Handicapped Individuals") #title
    # [DA7]:
    pie_df6 = rest_areas["HANDICAP"].value_counts() #get the series
    # [DA2]:
    pie_df6.sort_index(inplace=True) #sort by index
    pielabels6 = ["With Facilities for Handicapped Individuals"] #label
    piecolors6 = ["green"] #color
    pie_df6.plot(kind="pie", colors=piecolors6, autopct="%.1f%%", labels=pielabels6) #piechart
    plt.ylabel(" ") #removed the label "count" from the y axis
    st.pyplot()
    # checkbox for the table
    # [ST3]:
    showtable6 = st.checkbox("Check if you want to see the table for 'Percentage of Rest Areas with Facilities for Handicapped Individuals'")
    if showtable6:
        st.write(pie_df6)

with tab7:
    # [VIZ2]
    st.title("Percentage of Rest Areas with a Station for Recreational Vehicles") #title
    # [DA7]:
    pie_df7 = rest_areas["RV_STATION"].value_counts() #get the series
    # [DA2]:
    pie_df7.sort_index(inplace=True) #sort by index
    pielabels7 = ["Without a Station for Recreational Vehicles", "With a Station for Recreational Vehicles"] #label
    piecolors7 = ["red", "green"] #color
    pie_df7.plot(kind="pie", colors=piecolors7, autopct="%.1f%%", labels=pielabels7) #piechart
    plt.ylabel(" ") #removed the label "count" from the y axis
    st.pyplot()
    # checkbox for the table
    # [ST3]:
    showtable7 = st.checkbox("Check if you want to see the table for 'Percentage of Rest Areas with a Station for Recreational Vehicles'")
    if showtable7:
        st.write(pie_df7)

with tab8:
    # [VIZ2]
    st.title("Percentage of Rest Areas with an Area designated for Pets") #title
    # [DA7]:
    pie_df8 = rest_areas["PET_AREA"].value_counts() #get the series
    # [DA2]:
    pie_df8.sort_index(inplace=True) #sort by index
    pielabels8 = ["No Data", "With an Area designated for Pets"] #label
    piecolors8 = ["blue", "green"] #color
    pie_df8.plot(kind="pie", colors=piecolors8, autopct="%.1f%%", labels=pielabels8) #piechart
    plt.ylabel(" ") #removed the label "count" from the y axis
    st.pyplot()
    # checkbox for the table
    # [ST3]:
    showtable8 = st.checkbox("Check if you want to see the table for 'Percentage of Rest Areas with an Area designated for Pets'")
    if showtable8:
        st.write(pie_df8)