#Import libraries
import streamlit
import pandas

#App Title
streamlit.title('My Parents New Healthy Diner')

#Menu Header
streamlit.header('Breakfast Favorites')

#Menu Items
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.text('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#My Fruit List Dataframe
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)

#Let's put a pick list here so they can pick the fruits they want to include
streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))

#Display the table on the page
streamlit.dataframe(my_fruit_list)
