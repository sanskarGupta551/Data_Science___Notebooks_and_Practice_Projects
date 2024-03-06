import streamlit as st
import os
from sidebar import Sidebar



class Projects():
    def __init__(self):
        Sidebar.build_sidebar(self=self)
        self.build_projects()

    
    ## Build Projects Page
    ## (Contains Practice & Portfolio Projects each with their Seperate Presentation Streamlit WebApp)
    def build_projects(self):
        st.title("Data Science")
        st.header("Projects")

        

Projects()
