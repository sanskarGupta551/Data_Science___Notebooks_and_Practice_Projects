import streamlit as st
import os
from sidebar import Sidebar



class Notebooks():
    def __init__(self):
        Sidebar.build_sidebar(self=self)
        self.build_notebooks()

    
    ## Build Notes Page
    def build_notebooks(self):
        st.title("Data Science")
        st.header("Notebooks")
        


Notebooks()
