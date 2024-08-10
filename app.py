import streamlit as st
from streamlit_option_menu import option_menu

# The logo
st.logo("images/logo.png")

# Image
st.image("images/big_logo.png", width=650)

# The side bar
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'About Project', 'Contact'], 
        icons=['house', 'gear', 'phone'], menu_icon="cast", default_index=1)

# Main Page Menu
main_page_selection = option_menu(
    None, ["Home", "Order-Up", "Review Us", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

# Main - Home Page
if main_page_selection == "Home":
    st.markdown("""
## Welcome To :star2: Foody&Foodie :star2:
Foody & Foodie is an authentically modern restaurant in the heart of the city offering more than just a comfortable seat, wonderful ambience, and soothing  background noise.

Please check out our menu for cuisines from around the world.
                
Thank you for visiting our online store today.
                
Please leave a review on your way out.
""")

elif main_page_selection == "Order-Up":
    sweets_container = st.container(border=True)
    drinks_container = st.container(border=True)
    food_container = st.container(border=True)

    with sweets_container:
        col1, col2 = st.columns([3, 7], gap="small")

        with col1:
            st.image("images/muffin2.png")

        with col2:
            st.markdown(""" 
* ***Lemon Blueberry Muffins*** _$1.50_
* ***Chocolate Chip Muffins*** _$2.50_
* ***Strawberry Muffins*** _$3.25_
* ***Banana Muffins*** _$1.50_
* ***Strawberry Muffins*** _$5.50_
""")
            
    with drinks_container:
        col1, col2 = st.columns([7, 3], gap="small")

        with col2:
            st.image("images/coffee.png")

        with col1:
            st.markdown(""" 
* ***Cappuccino***      _$3.50_
* ***Latte***           _$3.50_
* ***Frappuccino***     _$3.50_
* ***Mocha***           _$3.50_
* ***Irish Coffee***    _$3.50_
""")

    with food_container:
        col1, col2 = st.columns([3, 7], gap="small")

        with col1:
            st.image("images/mittens.png")

        with col2:
            st.markdown(""" 
* ***Ugali le Choma*** _$11.50_
* ***Chips la Ketchup*** _$22.50_
* ***Ome du Fromage*** _$31.25_
* ***Kienyeji de Kuku*** _$15.50_
* ***Chapati Tacos la Beans*** _$25.50_
""")