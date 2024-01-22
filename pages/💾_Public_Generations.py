import streamlit as st
from database import *

"""
# 🚀 Public Generations
share your generations with the world!

---
"""
def draw_card(data: Generated):
    im, rest = st.columns([1, 2])

    try:
        im.image(data.image)
    except Exception:
        im.image('static/placeholder.jpg')

    rest.title(data.title)

    rest.write(data.text[:50] + "...")

    r1, r2 = rest.columns(2)
    r2.button("🎤 Poem" if data.type == 'poem' else '📖 Story', disabled=True, key=data.title+"status")

    if r1.button("🧑‍💻 Read Now...", type='primary', key=data.title):
        show_poem_story(data)

    st.write('---')

db = get_db()
for gen in db.get_all():
    data = Generated.from_dict(gen)

    draw_card(data)
