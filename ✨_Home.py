import streamlit as st

st.title("Story & Poem Reader")

pc, sc, hc = st.columns(3)

if pc.button("🎤 Generate Poem"):
    st.switch_page("pages/🎤_Poem_Gen.py")

if sc.button("Generate Story"):
    pass

if hc.button("My Generations"):
    pass
