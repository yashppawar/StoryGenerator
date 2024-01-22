import tinydb
import streamlit as st
from dataclasses import dataclass
import io
from typing import Literal
import base64

@dataclass
class Generated:
    image: io.BytesIO
    type: Literal['poem', 'story']
    text: str
    title: str
    published: bool = False

    def to_dict(self):
        return {
            'image': base64.b64encode(self.image.getvalue()).decode(),
            'type': self.type,
            'text': self.text,
            'title': self.title,
            'published': self.published,
        }

    @classmethod
    def from_dict(cls, data):
        image = io.BytesIO(base64.b64decode(data['image']))
        return cls(image, data['type'], data['text'], data['title'], data['published'])

class DataBase:
    def __init__(self):
        self.db =  tinydb.TinyDB('generated.json')

    def insert(self, data: Generated):
        data.published = True
        print(data.to_dict())
        self.db.insert(data.to_dict())

    def get_all(self):
        return self.db.all()
    
    def get_poems(self):
        item = tinydb.Query()
        return self.db.search(item.type == 'poem')
    
    def get_storys(self):
        item = tinydb.Query()
        return self.db.search(item.type == 'story')

def update_publish():
    st.session_state['data'].published = True

def show_poem_story(data: Generated):
    st.session_state['data'] = data
    st.switch_page('pages/✅_Generated.py')

@st.cache_resource
def get_db():
    return DataBase()
