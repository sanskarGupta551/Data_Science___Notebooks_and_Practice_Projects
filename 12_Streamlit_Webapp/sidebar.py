import streamlit as st 
import os 





class Sidebar(): # (Synced accross all pages and retains data even after closing the webapp)
    def __init__(self) -> None:
        pass 
    
    
    def build_sidebar(self): ## Build Sidebar 
        st.sidebar.title('Bookmarks') ## Bookmarking Notes/ Projects/ Tools    
        st.sidebar.title('Notes') ## Writing Notes to Self to remember
        st.sidebar.title('Account') ## Managing Account
