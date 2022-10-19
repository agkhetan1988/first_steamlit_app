#Import libraries
import streamlit
import pandas

#App Title
streamlit.title('My Mom\'s New Healthy Diner')

#Menu Header
streamlit.header('Breakfast Favorites')

#Menu Items
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.text('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#My Fruit List Dataframe
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a pick list here so they can pick the fruits they want to include
fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display the table on the page
streamlit.dataframe(fruits_to_show)

#New section to display fruitvice api response
streamlit.header('Fruityvice Fruity Advice!')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as table
streamlit.dataframe(fruityvice_normalized)
