import streamlit as st
import requests
from PIL import Image

'''
# smArt
'''
image = Image.open('/home/quan/code/qnguyen-gh/smArt/smArt/data/Abstract_Expressionism/jimmy-ernst_oracle-1971.jpg')
#open random image of test set

st.image(image)

user_input = st.selectbox('Select genre of the art piece',
('Abstract Expressionism',
 'Action painting',
 'Analytical Cubism',
 'Art Nouveau Modern',
 'Baroque',
 'Color Field Painting',
 'Contemporary Realism',
 'Cubism',
 'Early Renaissance',
 'Expressionism',
 'Fauvism',
 'High Renaissance',
 'Impressionism',
 'Mannerism Late Renaissance',
 'Minimalism',
 'Naive Art Primitivism',
 'New Realism',
 'Northern Renaissance',
 'Pointillism',
 'Pop Art',
 'Post Impressionism',
 'Realism',
 'Rococo',
 'Romanticism',
 'Symbolism',
 'Synthetic Cubism',
 'Ukiyo e'))

if st.button('Submit'):
    # print is visible in the server output, not in the page
    st.write('Ideally now the output of the model will be output')
else:
    st.write('C\'mon click me b***h')
