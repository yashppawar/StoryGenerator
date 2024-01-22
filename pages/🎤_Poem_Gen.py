import streamlit as st
from helpers import *

"""
# Poem Generator
"""
poem_topic = st.text_input("Topic: ")

if st.button("✨ Generate"):
    with st.spinner("Generating..."):
        story = generate_text(poem_topic, POEM)
        image = generate_image(poem_topic)

    st.image(image)
    st.write(story)
