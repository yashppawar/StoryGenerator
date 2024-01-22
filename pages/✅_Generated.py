import streamlit as st
import tempfile
from gtts import gTTS
from database import *

c1, c2 = st.columns(2)

if 'data' not in st.session_state:
    st.error("Nothing to show here! generate something")
    pc, sc, hc = st.columns(3)

    if pc.button("🎤 Generate Poem"):
        st.switch_page("pages/🎤_Poem_Gen.py")

    if sc.button("📖 Generate Story"):
        st.switch_page("pages/📖_Story_Gen.py")

    if hc.button("🚀 Public Generations"):
        st.switch_page("pages/💾_Public_Generations.py")

else:
    data = st.session_state.data

    try: 
        c2.image(data.image)
    except Exception:
        pass

    c1.title(data.title)

    c1a, c1b = c1.columns(2)
    # c1a.info(data.type, icon="🎤" if data.type == 'poem' else "📖")
    c1a.button("🎤 Poem" if data.type == 'poem' else '📖 Story', disabled=True)

    if not data.published:
        if c1b.button("🚀 Publish"):
            db = DataBase()
            db.insert(data)
            update_publish()
            st.toast("Published 🚀")
    else:
        c1b.button("🚀 Published", disabled=True)

    st.write("---")

    if data.type == 'poem':
        _, poem_col, _ = st.columns([1, 2, 1])
        poem_col.write(data.text)
    else:
        st.write(data.text)


    c1.write("let me read it for you:")
    st.toast("Recording Audio... 🎤")
        
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tp:
        tts = gTTS(data.text)
        tts.save(tp.name)
        c1.audio(tp.name)
        st.toast("Audio Recorded 🔊")

