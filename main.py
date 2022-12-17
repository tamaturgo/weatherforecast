from program import app, writeData
import streamlit as st
from multiapp import MultiApp
from apps import read, confirm

app = MultiApp()

# Add all your application here
app.add_app("Read", read.app)
app.add_app("Confirm", confirm.app)
# The main app

app.run("Read")
app.open("Confirm")