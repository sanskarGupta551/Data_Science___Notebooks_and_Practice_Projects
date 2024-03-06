import streamlit as st
import os
from sidebar import Sidebar



class Tools_and_Workflows():
    def __init__(self):
        Sidebar.build_sidebar(self=self)
        self.build_tools_and_workflows()

    
    ## Build Tools & Workflows Page 
    ## (Contains Ease of life Tools & Automation Workflows for Data Science)
    def build_tools_and_workflows(self):
        st.title("Data Science")
        st.header("Tools & Workflows")

        

Tools_and_Workflows()
