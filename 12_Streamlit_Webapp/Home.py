import streamlit as st
import os



class webapp():
    def __init__(self):
        self.sidebar()
        self.build_home()
        
    
    ## Build Home Page
    def build_home(self):
        st.title("Data Science")
        st.header("Home")


    ## Build Sidebar (Synced accross all pages and retains data even after closing the webapp)
    def sidebar(self):
        st.sidebar.title('Bookmarks')
        st.sidebar.title('Notes')
        st.sidebar.title('Account')
        


webapp()
