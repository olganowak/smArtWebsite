import streamlit as st
import pandas as pd
import numpy as np
import random
import requests
from PIL import Image
#import matplotlib.pyplot as plt

'''
# smArt
'''

## Extract image and genre from test set
# retrieve DataFrame and npy-file (for image arrays)
test_set = pd.read_csv("/Users/olganowak/code/olganowak/smArt/raw_data/drive-download-20220606T150142Z-001/4_class_v01.csv")
test_npy=np.load("/Users/olganowak/code/olganowak/smArt/raw_data/drive-download-20220606T150142Z-001/4_class_v01.npy")
# get amount of rows and generate random index (row to get image from)
rows=test_set.shape[0]
if "index" not in st.session_state.keys():
    st.session_state["index"] = random.randint(0,rows)
# open and show random image of test set
image = Image.open(f'/Users/olganowak/code/olganowak/smArt/raw_data/wikiart/{test_set["path"][st.session_state["index"]]}')
st.image(image)

# retrieve corresponding genre and array
real_genre = [test_set["genre"][st.session_state["index"]]]
image_array = test_npy[st.session_state["index"]]
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

## Trigger model
# Initialize state
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False
def callback():
    # at this point the button was clicked
    st.session_state.button_clicked = True
# make user commit to decision
if st.button('Submit', on_click=callback) or st.session_state.button_clicked:
    columns = st.columns(2)
    # columns = st.columns(2)
    # shove image into pipeline (gets reshaped and put through model) and predict genre
    columns[0].markdown("""## Your answer:""")
    columns[0].write(user_input)

    columns[1].markdown('''## The model\'s prediction:''')
    # PLUG API TO RUN MODEL ON THE IMAGE
    url= "http://127.0.0.1:8000/predict"

    #params="/home/quan/code/qnguyen-gh/smArt/smArt/data/wikiart/Expressionism/Expressionism/abidin-dino_drawing-pain-1968.jpg"

    #params= f'{test_set["genre"][st.session_state["index"]]}/{test_set["path"][st.session_state["index"]]}'
    genre, filename = test_set["path"][st.session_state["index"]].split("/")
    params={"genre":genre,"filename":filename}

    response=requests.get(url,params=params)
    st.write(response.json())
    # display real genre
    '''
    ## The real genre is...
    '''
    if st.button('Pressure is on, click to find out'):
        # real result gets output (retrieved from test set)
        st.write(real_genre[0])
    else:
        pass
else:
    # message for the user if the button is not clicked
    #st.write('C\'mon click me b***h')
    pass

# get response on performance
# Feedback on performance, e.g. different formats if correct or incorrect')
