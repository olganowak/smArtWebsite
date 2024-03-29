import streamlit as st
import pandas as pd
import random
import requests
from PIL import Image
import time
#import pyautogui
import hydralit_components as hc
from streamlit_option_menu import option_menu

st.markdown("<h1 style='text-align: center;'>F A P ©</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Fine Art Painting Classification</h5>", unsafe_allow_html=True)
st.text("")
st.caption("<h6 style='text-align: center;'>Test your knowledge against a machine</h6>", unsafe_allow_html=True)

    ## Extract image and genre from test set

# retrieve DataFrame
#test_set = pd.read_csv("https://storage.googleapis.com/artdataset/sample_dataframe.csv")
test_set = pd.read_csv("https://storage.googleapis.com/artdataset/predictions_dataframe.csv")
# get amount of rows and generate random index (row to get image from)
rows=test_set.shape[0]
if "index" not in st.session_state.keys():
    st.session_state["index"] = random.randint(0,rows)
# open and show random image of test set
im_url=test_set["url"][st.session_state["index"]]
image = Image.open(requests.get(im_url, stream=True).raw)
columns = st.columns([1,3,1])
columns[1].image(image)
# retrieve corresponding genre
real_genre = [test_set["genre"][st.session_state["index"]].replace("_"," ")]

    ## Get user input

# full list of available genres
genre_list = ['Abstract Expressionism',
 'Art Nouveau Modern',
 'Baroque',
 'Color Field Painting',
 'Cubism',
 'Expressionism',
 'Impressionism',
 'Naive Art Primitivism',
 'Northern Renaissance',
 'Pop Art',
 'Post Impressionism',
 'Realism',
 'Rococo',
 'Romanticism',
 'Symbolism']
# create new list removing real_genre to avoid duplicates
genre_list.remove(real_genre[0])
# provide 4 genres to select from as user input (real genre, from test set + 3 other randomly generated genre)
if "choices" not in st.session_state.keys():
    st.session_state["choices"] = random.sample(random.sample(genre_list,3) + real_genre,4)
# get user input
user_input = st.selectbox('Which genre is it?',
(st.session_state["choices"][0],st.session_state["choices"][1],st.session_state["choices"][2],st.session_state["choices"][3]))

# # PLUG API TO RUN MODEL ON THE IMAGE
# # shove image into pipeline (gets reshaped and put through model) and predict genre
# url= "http://127.0.0.1:8000/predict"
# # get params
# filename = test_set["filename"][st.session_state["index"]]
# genre = test_set["genre"][st.session_state["index"]]
# params={"genre":genre,"filename":filename}
# #if "spinner" not in st.session_state.keys():
# #    st.session_state["spinner"] = st.spinner("Prediction is loading . . .  Please stand by, Davy is doing his thing")
# #with st.session_state["spinner"]:
# with st.spinner("Prediction is loading . . .  Please stand by, Davy is doing his thing"):
#     if "response" not in st.session_state.keys():
#         st.session_state["response"] = requests.get(url,params=params).json()
# prediction = st.session_state["response"]

    ## Trigger model

# Initialize state
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False
def callback():
    # at this point the button was clicked
    st.session_state.button_clicked = True
# make user commit to decision
if st.button('Submit', on_click=callback) or st.session_state.button_clicked:
    columns = st.columns([2,3])
    # display answer and model prediction
    columns[0].markdown("""## Your answer:""")
    columns[0].write(user_input)
    columns[1].markdown('## The model\'s prediction:')
    # get prediction
    prediction = test_set["predictions"][st.session_state["index"]]
    if "spinner" not in st.session_state.keys():
        st.session_state["spinner"] = st.spinner("Davy making a prediction, please stand by. . .")
        with st.session_state["spinner"]:
            if "timer" not in st.session_state.keys():
                st.session_state["timer"] = time.sleep(4)
    columns[1].write(prediction)
    st.text("")
    # display real genre
    columns = st.columns(2)
    columns[0].markdown("""## The real genre is...""")
    if st.button('Pressure is on, click to find out'):
        # real result gets output (retrieved from test set)
        columns[1].markdown(f"## _{real_genre[0]}_")
        if user_input == prediction and prediction == real_genre[0]:
            st.success("Y'all both good")
        elif user_input == real_genre[0] and prediction != real_genre[0]:
            st.balloons()
            st.success("Congrats, you beat the model!")
        elif user_input != real_genre[0] and prediction == real_genre[0]:
            st.error("The machine beat you. Doomsday is coming...")
        else:
            st.error("Damn y'all both suck!")
        st.text("")
        # display title and artist of art piece
        title = test_set["title"][st.session_state["index"]]
        st.markdown(f"Title: *{title}*")
        artist = test_set["artist"][st.session_state["index"]]
        st.markdown(f"Artist: *{artist}*")
        st.text("")
        st.caption("<h6 style='text-align: center;'>Reload the page to try again!</h6>", unsafe_allow_html=True)
    else:
        pass
else:
    pass
