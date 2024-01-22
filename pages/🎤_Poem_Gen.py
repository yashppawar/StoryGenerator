import streamlit as st
from helpers import *
from gtts import gTTS
import tempfile

"""
# Poem Generator
"""
poem_topic = st.text_input("Topic: ")

if st.button("✨ Generate"):
    with st.spinner("Generating..."):
        data = generate_metadata(poem_topic, POEM)
        poem = generate_text(data['text'])
        image = generate_image(data['image'])

    c1, c2 = st.columns(2)

    try: 
        c2.image(image)
    except Exception:
        pass
    
    c1.title(data['title'])

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tp:
        tts = gTTS(poem)
        tts.save(tp.name)
        c1.audio(tp.name)

    _, poem_col, _ = st.columns([1, 2, 1])
    poem_col.write(poem)

