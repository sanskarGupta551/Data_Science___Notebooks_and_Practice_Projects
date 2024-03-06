import streamlit as st
import os
from sidebar import Sidebar # Sidebar Module 
import sys 
sys.path += ['./0_Home', './1_Notebooks', './2_Projects', './3_Tools_and_Workflows']

from Data_Science_Methodology_1_1 import Data_Science_Methodology # Notebooks Modules





class home(): # (Contains Intro, Documentation, Guides & Other Basic Information)
    def __init__(self):
        Sidebar.build_sidebar(self=self)
        self.build_home()
        
    
    def build_home(self): # Build Home Page
        st.title("Data Science")
        st.header("Home")
        st.divider()
        




home()
