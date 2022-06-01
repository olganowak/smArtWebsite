import streamlit as st
import random
import requests
from PIL import Image

'''
# smArt
'''

## Extract image and genre from test set

# open and show random image of test set
image = Image.open('/home/quan/code/qnguyen-gh/william-congdon_the-black-city-i-new-york-1949.jpg')
st.image(image)
# retrieve corresponding genre
real_genre = ['some genre']

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

# provide 4 genres to select from as user input (real genre, from test set + 3 other randomly generated genre)
if "choices" not in st.session_state.keys():
    st.session_state["choices"] = random.sample(random.sample(genre_list,3) + real_genre,4)

# get user input
user_input = st.selectbox('Select genre of the art piece',
(st.session_state["choices"][0],st.session_state["choices"][1],st.session_state["choices"][2],st.session_state["choices"][3]))
## Trigger model

# make user commit to decision
# Initialize state
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False
def callback():
    # at this point the button was clicked
    st.session_state.button_clicked = True

if st.button('Submit', on_click=callback) or st.session_state.button_clicked:
    columns = st.columns(2)
    # columns = st.columns(2)
    # shove image into pipeline (gets reshaped and put through model) and predict genre
    columns[0].markdown("""## Your answer:""")
    columns[0].write(user_input)

    columns[1].markdown('''## The model\'s prediction:''')
    columns[1].write(real_genre[0])
    '''
    ## The real genre is...
    '''
    if st.button('Pressure is on, click to find out'):
        # real result gets output (retrieved from test set)
        st.write(real_genre[0])
    else:
        pass
    # get response on performance
    # Feedback on performance, e.g. different formats if correct or incorrect')
else:
    # message for the user if the button is not clicked
    #st.write('C\'mon click me b***h')
    pass
