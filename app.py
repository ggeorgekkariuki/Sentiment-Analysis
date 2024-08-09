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