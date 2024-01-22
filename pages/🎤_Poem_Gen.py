import streamlit as st
from helpers import *
from database import *

"""
# Poem Generator
"""

st.image('static/feather-ink.jpeg')

poem_topic = st.text_input("Topic: ")

if st.button("✨ Generate"):
    with st.spinner("Generating..."):
        data = generate_metadata(poem_topic, POEM)
        poem = generate_text(data['text'])
        image = generate_image(data['image'])

    show_poem_story(Generated(image, 'poem', poem, data['title']))
