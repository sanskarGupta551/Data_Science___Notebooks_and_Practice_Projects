import streamlit as st
import os
from sidebar import Sidebar



class webapp():
    def __init__(self):
        Sidebar.build_sidebar(self=self)
        self.build_home()
        
    
    ## Build Home Page
    def build_home(self):
        st.title("Data Science")
        st.header("Home")



webapp()
