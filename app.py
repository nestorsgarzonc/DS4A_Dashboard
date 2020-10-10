import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
# CUSTOM WIDGETS
import sidebar as sd
import os

df = pd.read_csv('Follow_Up_San_Diego.csv')

state_sidebar = sd.sidebar()

st.title('Offcorss DS4A 😎')

st.write(df)
st.line_chart(df)

img_file_buffer = st.file_uploader("Upload a video", type=["avi", "mp4"])
