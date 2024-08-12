import streamlit as st
from streamlit_option_menu import option_menu
import time
import numpy as np
from classes import execute_flow

# The logo
st.logo("images/logo.png")

# Image
st.image("images/big_logo.png", width=650)

# Main Page Menu
main_page_selection = option_menu(
    None, ["Home", "Order-Up", "Review Us"], 
    icons=['house', 'cloud-upload', "list-task"], 
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
* ***Lemon Blueberry Muffins*** _A fabulously fab muffin only at **$1.50**_
* ***Chocolate Chip Muffins*** _An exquisitly exquisit muffin only at **$2.50**_
* ***Strawberry Muffins*** _A wonderful wonder of a muffin only at **$3.25**_
* ***Banana Muffins*** _A beautiful beauty of a muffin only at **$1.50**_
* ***Strawberry Muffins*** _A miraculous miracle of a muffin only at **$5.50**_
""")
            
    with drinks_container:
        col1, col2 = st.columns([7, 3], gap="small")

        with col2:
            st.image("images/coffee.png")

        with col1:
            st.markdown(""" 
* ***Cappuccino***   _Yumminess redifined so well in a futuristic cup **$8.50**_
* ***Latte***        _Visionary redifined so well in a futuristic cup **$6.50**_
* ***Frappuccino***  _Impossibility redifined so well in a futuristic cup **$5.50**_
* ***Mocha***        _Creativity redifined so well in a futuristic cup **$2.50**_
* ***Irish Coffee*** _Soberness redifined so well in a futuristic cup **$4.50**_
""")

    with food_container:
        col1, col2 = st.columns([3, 7], gap="small")

        with col1:
            st.image("images/mittens.png")

        with col2:
            st.markdown(""" 
* ***Ugali le Choma*** _Food so yummy, you could slap your mom **$11.50**_
* ***Chips la Ketchup*** _Food so yummy, you should slap your dad **$22.50**_
* ***Ome du Fromage*** _Food so yummy, you could slap youself **$31.25**_
* ***Kienyeji de Kuku*** _Food so yummy, you shall slap your bro $15.50_
* ***Chapati Tacos la Beans*** _Food so yummy, we slap you $25.50_
""")

elif main_page_selection == "Review Us":
    # The Form Container
    tweet_container = st.empty()

    with tweet_container.container():

        col1, col2 = st.columns([7,3])

        with col1:
            st.subheader("Review Us:bird:")
            with st.form(key='form1'):
                username = st.text_input("Username", placeholder="Enter your Username")
                sentiment = st.text_area("Review", placeholder="Please enter your review here")
                predict_button = st.form_submit_button('Post Review')


        with col2:
                st.subheader("The Back End Prediction :telescope:")
                info_text = st.info("Enter text to predict sentiment")
                if predict_button:
                    info_text.empty()
                    if username == "" and sentiment == "":
                        st.error("Please fill in the previous form - Username and Review Fields")
                    elif username == "":
                        st.info("Please fill in the previous form - Username Field", icon="ℹ️")
                    elif sentiment == "":
                        st.info("Please fill in the previous form - Review Field", icon="ℹ️")
                    else:
                        st.write(f"The user @{username.lower().replace(' ', '_')} said '{sentiment}'")
                        randoms = ['Thinking', 'Processing', 'Considering', 'Wizardy Applying', 'Hmmm', 'Contacting the Mothership', "Predicting",
                        "Checking under the bed for an answer"]
                        answers = randoms[np.random.choice(len(randoms))]
                        with st.spinner(f"{answers}..."):
                            time.sleep(3)
                            st.success(f"Our model predicted the review to be a {execute_flow(sentiment)} Sentiment!")