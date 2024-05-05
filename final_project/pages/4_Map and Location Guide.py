"""
Name:    Anna Szenas
CS230:   CS230-5
Data:    Rest Areas In California
URL:

Description:

This program creates one page for the Streamlit webpage, describing the Rest Areas In California. On this page
users can select either 'all rest areas' or rest areas with specific facilities and the webpage displays the rest
areas of their choices either on a scatterplot map or on an iconmap.
"""

import pandas as pd
import streamlit as st
import pydeck as pdk

#my path:
path = "C:/Users/Felhasználó/Desktop/Annaa/corvinus/6. semester bentley/intro to python/codes/pythonProject/final_project/"

st.set_option('deprecation.showPyplotGlobalUse', False)

#reading the dataframe:
rest_areas = pd.read_csv(path + "Rest_Areas.csv")

#[DA1]:
rest_areas.dropna(inplace=True)
rest_areas.rename(columns={"LATITUDE":"lat", "LONGITUDE": "lon"}, inplace= True)

#page title:
st.title("Exploring Rest Areas in California: Map and Location Guide")

#description:
'''
Page Summary:
'''
'''
This page allows you to discover rest areas across various amenities and locations. You can explore all rest areas, 
displaying their locations on the map, or locate rest areas equipped with restroom, water or phone facilities. You 
can discover rest areas with picnic tables for outdoor dining or with vending machines for snacks and drinks. You 
can locate rest areas with facilities for handicapped individuals or rest areas with designated RV stations as well.
In addition, you can find rest areas with areas for pets to rest and play.
'''
#creating radio buttons for the map:------------------------------------------------------------------------------------
map_options = ["All Rest Areas",
               "Rest Areas with Restrooms",
               "Rest Areas with Water",
               "Rest Areas with Picnic Tables",
               "Rest Areas with Phone",
               "Rest Areas with Vending Machines",
               "Rest Areas with Facilities for Handicapped Individuals",
               "Rest Areas with a Station for Recreational Vehicles",
               "Rest Areas with an Area designated for Pets"]
#[ST2]:
choosen_map = st.radio("Select a Map from the list:", options=map_options)

#creating new dataframes for the maps:----------------------------------------------------------------------------------
#[DA4]:
restroom_df = rest_areas[rest_areas["RESTROOM"].str.upper() == "YES"]
#[DA4]:
water_df = rest_areas[rest_areas["WATER"].str.upper() == "YES"]
#[DA4]:
picnic_df = rest_areas[rest_areas["PICNICTAB"].str.upper() == "YES"]
#[DA4]:
phone_df = rest_areas[rest_areas["PHONE"].str.upper() == "YES"]
#[DA4]:
vending_df = rest_areas[rest_areas["VENDING"].str.upper() == "YES"]
#[DA4]:
handicap_df = rest_areas[rest_areas["HANDICAP"].str.upper() == "YES"]
#[DA4]:
rv_df = rest_areas[rest_areas["RV_STATION"].str.upper() == "YES"]
#[DA4]:
pet_df = rest_areas[rest_areas["PET_AREA"].str.upper() == "YES"]

#all areas map:---------------------------------------------------------------------------------------------------------
#[VIZ3] - scatterplot map
#create the viewstate:
all_view_state = pdk.ViewState(
    latitude=rest_areas["lat"].mean(),  #the latitude of the view center - CENTER
    longitude=rest_areas["lon"].mean(),  #the longitude of the view center - CENTER
    zoom=5,  #view zoom level
    pitch=0)  #tilt level

#create layers:
all_layer1 = pdk.Layer(type="ScatterplotLayer",  #layer type
                       data=rest_areas,  #data
                       get_position="[lon, lat]",  #coordinates
                       get_radius = 10000,  #scatter radius - adjust size
                       get_color=[255, 0, 0],  #scatter color - color code for red
                       pickable=True  #work with tooltip
                       )

all_layer2 = pdk.Layer(type="ScatterplotLayer",  #layer type
                       data=rest_areas,  #data
                       get_position="[lon, lat]",  #coordinates
                       get_radius=5000,  #scatter radius - adjust size
                       get_color=[255, 165, 0],  #scatter color - color code for orange
                       pickable=True  #work with tooltip
                       )

#create tooltip:
all_tool_tip = {"html": "Rest Area Name:<br/> <b>{NAME}</b>",
                "style": {"backgroundColor": "black",
                          "color": "white"}
                }

#create map:
all_map = pdk.Deck(
    map_style="mapbox://styles/mapbox/satellite-streets-v12",
    initial_view_state=all_view_state,  #viewstate
    layers=[all_layer1, all_layer2],  #layers
    tooltip=all_tool_tip  #tooltip
)

#icon maps:-------------------------------------------------------------------------------------------------------------
#i created a function which creates the iconmap
#inputs are the urls of the icons and the dataframe of the map

#[PY3]: a function, that I wrote and returns a value - I used it 8 times, I will document the usages with "[PY3]-U"
def create_iconmap(icon_url,dataframe):
    #[VIZ4] - iconmap
    #first the function should format the icon
    icon_data = {
        "url": icon_url,
        "width": 100,
        "height": 100,
        "anchorY": 1  #how far away do i want to put your icon
    }

    #then the function adds the icons to the dataframe
    #[DA9]:
    dataframe["icon_data"] = None  #new column with first nothing
    for i in dataframe.index:
        dataframe["icon_data"][i] = icon_data

    #the function creates the layer with the custom icon
    icon_layer = pdk.Layer(type="IconLayer",
                           data=dataframe,
                           get_icon="icon_data",  # where we get this icon from
                           get_position="[lon,lat]",
                           get_size=13,
                           pickable=True)

    #then viewstate:
    icon_view_state = pdk.ViewState(
        latitude=dataframe["lat"].mean(),
        longitude=dataframe["lon"].mean(),
        zoom=5, #same zoom as the allmap
        pitch=0
    )

    #tooltip:
    icon_tool_tip = {"html": "Rest Area Name:<br/> <b>{NAME}</b>",
                "style": {"backgroundColor": "black",
                          "color": "white"}
                }

    icon_map = pdk.Deck(
        map_style="mapbox://styles/mapbox/satellite-streets-v12",
        layers=[icon_layer],
        initial_view_state=icon_view_state,
        tooltip=icon_tool_tip
    )

    return icon_map

#creating url list and dataframe list for the icons:--------------------------------------------------------------------
iconlist = ["https://upload.wikimedia.org/wikipedia/commons/8/8f/Toilets_unisex.svg",
            "https://upload.wikimedia.org/wikipedia/commons/c/cd/Waterbody.svg",
            "https://upload.wikimedia.org/wikipedia/commons/b/be/Picnic_Table_Icon.svg",
            "https://upload.wikimedia.org/wikipedia/commons/1/1f/Phoneicon.svg",
            "https://upload.wikimedia.org/wikipedia/commons/3/32/Noun44656_vending_machine.svg",
            "https://upload.wikimedia.org/wikipedia/commons/3/31/Wheelchair-green3.svg",
            "https://upload.wikimedia.org/wikipedia/commons/1/15/Rv-site.svg",
            "https://upload.wikimedia.org/wikipedia/commons/a/a1/Dog-1800633.svg"]

df_list = [restroom_df, water_df, picnic_df, phone_df, vending_df, handicap_df, rv_df, pet_df]

#showing the maps:------------------------------------------------------------------------------------------------------
if choosen_map == "All Rest Areas":
    # show the all_map and title
    st.title("All Rest Areas:")
    st.pydeck_chart(all_map)

elif choosen_map == "Rest Areas with Restrooms":
    #show title + map:
    st.title("Rest Areas with Restrooms:")
    #[PY3]-U:
    iconmap1 = create_iconmap(icon_url=iconlist[0],dataframe=df_list[0])
    st.pydeck_chart(iconmap1)

elif choosen_map == "Rest Areas with Water":
    #show title + map:
    st.title("Rest Areas with Water:")
    # [PY3]-U:
    iconmap2 = create_iconmap(icon_url=iconlist[1],dataframe=df_list[1])
    st.pydeck_chart(iconmap2)

elif choosen_map == "Rest Areas with Picnic Tables":
    st.title("Rest Areas with Picnic Tables:")
    # [PY3]-U:
    iconmap3 = create_iconmap(icon_url=iconlist[2], dataframe=df_list[2])
    st.pydeck_chart(iconmap3)

elif choosen_map == "Rest Areas with Phone":
    st.title("Rest Areas with Phone:")
    # [PY3]-U:
    iconmap4 = create_iconmap(icon_url=iconlist[3], dataframe=df_list[3])
    st.pydeck_chart(iconmap4)

elif choosen_map == "Rest Areas with Vending Machines":
    st.title("Rest Areas with Vending Machines:")
    # [PY3]-U:
    iconmap5 = create_iconmap(icon_url=iconlist[4], dataframe=df_list[4])
    st.pydeck_chart(iconmap5)

elif choosen_map == "Rest Areas with Facilities for Handicapped Individuals":
    st.title("Rest Areas with Facilities for Handicapped Individuals:")
    # [PY3]-U:
    iconmap6 = create_iconmap(icon_url=iconlist[5], dataframe=df_list[5])
    st.pydeck_chart(iconmap6)

elif choosen_map == "Rest Areas with a Station for Recreational Vehicles":
    st.title("Rest Areas with a Station for Recreational Vehicles:")
    # [PY3]-U:
    iconmap7 = create_iconmap(icon_url=iconlist[6], dataframe=df_list[6])
    st.pydeck_chart(iconmap7)

elif choosen_map == "Rest Areas with an Area designated for Pets":
    st.title("Rest Areas with an Area designated for Pets:")
    # [PY3]-U:
    iconmap8 = create_iconmap(icon_url=iconlist[7], dataframe=df_list[7])
    st.pydeck_chart(iconmap8)






