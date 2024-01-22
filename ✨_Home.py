import streamlit as st

st.title("Story & Poem Generator")
st.subheader("& Reader")

pc, sc, hc = st.columns(3)

if pc.button("🎤 Generate Poem"):
    st.switch_page("pages/🎤_Poem_Gen.py")

if sc.button("📖 Generate Story"):
    st.switch_page("pages/📖_Story_Gen.py")

if hc.button("🚀 Public Generations"):
    st.switch_page("pages/💾_Public_Generations.py")

st.image('static/ai-story-gen.png')
