import streamlit as st
import os



class Projects():
    def __init__(self):
        self.sidebar()
        self.build_projects()

    
    ## Build Projects Page
    def build_projects(self):
        st.title("Data Science")
        st.header("Projects")

    
    ## Build Sidebar (Synced accross all pages and retains data even after closing the webapp)
    def sidebar(self):
        st.sidebar.title('Bookmarks')
        st.sidebar.title('Notes')
        st.sidebar.title('Account')
        
        

Projects()
