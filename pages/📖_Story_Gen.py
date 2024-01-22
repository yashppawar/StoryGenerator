import streamlit as st
from helpers import *
from database import *

"""
# Story Generator
"""

st.image('static/story.jpg')

story_topic = st.text_input("Topic: ")

if st.button("✨ Generate"):
    with st.spinner("Generating..."):
        data = generate_metadata(story_topic, STORY)
        story = generate_text(data['text'])
        image = generate_image(data['image'])

    show_poem_story(Generated(image, 'story', story, data['title']))
