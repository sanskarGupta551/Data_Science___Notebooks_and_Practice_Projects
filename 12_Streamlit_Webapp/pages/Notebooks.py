import streamlit as st
import os
from sidebar import Sidebar



class Notebooks():
    def __init__(self):
        Sidebar.build_sidebar(self=self)
        self.build_notebooks()

    
    ## Build Notebooks Page
    ## (Contains Data Science Topics explained with great Visualization and
    ##  easy-to-read & understand Bite sized informations)
    def build_notebooks(self):
        st.title("Data Science")
        st.header("Notebooks")
        


Notebooks()
