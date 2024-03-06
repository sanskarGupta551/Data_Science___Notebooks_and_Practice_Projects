import streamlit as st
import os



class Tools_and_Workflows():
    def __init__(self):
        self.sidebar()
        self.build_tools_and_workflows()

    
    ## Build Tools & Workflows Page
    def build_tools_and_workflows(self):
        st.title("Data Science")
        st.header("Tools & Workflows")


    ## Build Sidebar (Synced accross all pages and retains data even after closing the webapp)
    def sidebar(self):
        st.sidebar.title('Bookmarks')
        st.sidebar.title('Notes')
        st.sidebar.title('Account')
        
        

Tools_and_Workflows()
