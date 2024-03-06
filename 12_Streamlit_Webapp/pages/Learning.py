import streamlit as st
import os
from PIL import Image
from sidebar import Sidebar
import base64





class Learning(): # (Contains Data Science Topics explained with great Visualization and 
                   # easy-to-read & understand Bite sized informations along with Projects)
    def __init__(self): 
        self.topic_class=0
        Sidebar.build_sidebar(self=self)
        self.build_learning()

    
    def build_learning(self): # Build Learning Page
        st.title("Data Science")
        st.header("Learning")
        self.topics_multiselect()
        self.show_widget()
    
    
    def topics_multiselect(self): # Builds a Multi-select widget for Data Science Topics
        self.selected_topics = st.multiselect("Topics: ", # Notebook Topics Tab
                                             ["**Projects",  
                                              "**Notebooks",
                                              "Data Science Methodology", 
                                              "Data Collection",
                                              "Database & SQL", 
                                              "Data Analysis",
                                              "Data Visualization",
                                              "Machine Learning",
                                              "Deep Learning",
                                              "Generative Ai",
                                              "Reinforcement Learning",
                                              "MLOps"], 
                                              placeholder="Filter Learning Resources",)
        st.divider()
        
        
        #for tags in self.selected_topics(): # Check if tags present in projects/notebooks 
        #    if tags in widget.tags(): show_widgets


    def show_widget(self):
        # Load your image
        image = Image.open(r"C:\Users\Sanskar\OneDrive\Pictures\Screenshots\1-notebook.png")
        # Display the image with a caption
        st.image(image, width=240)
        



Learning()
