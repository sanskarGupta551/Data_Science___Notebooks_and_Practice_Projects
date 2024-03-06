import streamlit as st
import os
import sys 
sys.path += ['./0_Home', './1_Notebooks', './2_Projects', './3_Tools_and_Workflows']

from sidebar import Sidebar





class webapp():
    def __init__(self):
        Sidebar.build_sidebar(self=self)
        self.build_home()
        
    
    ## Build Home Page 
    ## (Contains Intro, Documentation, Guides & Other Basic Information)
    def build_home(self):
        st.title("Data Science")
        st.header("Home")



webapp()
