import streamlit as st
import os



class Notes():
    def __init__(self):
        self.sidebar()
        self.build_notes()

    
    ## Build Notes Page
    def build_notes(self):
        st.title("Data Science")
        st.header("Notes")
        
    
    ## Build Sidebar (Synced accross all pages and retains data even after closing the webapp)
    def sidebar(self):
        st.sidebar.title('Bookmarks')
        st.sidebar.title('Notes')
        st.sidebar.title('Account')



Notes()
