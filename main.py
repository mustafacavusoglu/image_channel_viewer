import os
import cv2
import tifffile as tff
import numpy as np
import pandas as pd
import streamlit as st

@st.cache
def read_image(image_name:str, channels:list)-> np.array:
    image = tff.imread(image_name)
    return image[:,:,channels], image.shape[-1]


st.session_state.index = 0
st.session_state.channel_count = 3
st.session_state.image_path = 'images-4/'

c1, c2, c3 = st.columns([1, 4, 1])


with c2:
    
    img_area = st.image(np.zeros((512,512,3)))
    
    

    st.session_state.image_path = st.selectbox(
    "Which Folder You Want?",
    (i + '/' for i in os.listdir() if os.path.isdir(i))
    
)
    st.session_state.image_list = [st.session_state.image_path + i for i in os.listdir(st.session_state.image_path)]



    st.session_state.image_name =  st.selectbox(
            "Select Image",
            (st.session_state.image_list)
            
        )

    st.session_state.index = st.session_state.image_list.index(st.session_state.image_name)
    st.session_state.default_image, st.session_state.channel_count = read_image(st.session_state.image_list[st.session_state.index], [0,1,2])
    img_area.image(st.session_state.default_image, width=512)

    st.session_state.multi_selection = st.multiselect(
    "Which channels will show?",
    range(0, st.session_state.channel_count),
    max_selections=3,    
)


if len(st.session_state.multi_selection) == 1:
    st.session_state.default_image, st.session_state.channel_count = read_image(st.session_state.image_list[st.session_state.index], [st.session_state.multi_selection[0], st.session_state.multi_selection[0], st.session_state.multi_selection[0]])
    img_area.image(st.session_state.default_image, width=512)

if len(st.session_state.multi_selection) == 2:
    st.session_state.default_image, st.session_state.channel_count = read_image(st.session_state.image_list[st.session_state.index], [st.session_state.multi_selection[0], st.session_state.multi_selection[1], st.session_state.multi_selection[0]])
    img_area.image(st.session_state.default_image, width=512)

if len(st.session_state.multi_selection) == 3:
    st.session_state.default_image, st.session_state.channel_count = read_image(st.session_state.image_list[st.session_state.index], st.session_state.multi_selection)
    img_area.image(st.session_state.default_image, width=512)

if len(st.session_state.multi_selection) == 0:
    st.session_state.default_image, st.session_state.channel_count = read_image(st.session_state.image_list[st.session_state.index], [0,1,2])
    img_area.image(st.session_state.default_image, width=512)