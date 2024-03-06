import streamlit as st 
import os 



class Sidebar():
    def __init__(self) -> None:
        pass 
    
    
    ## Build Sidebar (Synced accross all pages and retains data even after closing the webapp)
    def build_sidebar(self):
        ## Bookmarking Notes/ Projects/ Tools    
        st.sidebar.title('Bookmarks')
        ## Writing Notes to Self to remember
        st.sidebar.title('Notes')
        ## Managing Account
        st.sidebar.title('Account')
