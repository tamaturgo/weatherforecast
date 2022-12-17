"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self, startPage):

        # get the app
        for app in self.apps:
            if app['title'] == startPage:
                app['function']()
                break

    def open(self, page):
        
        # Close the current page
        for app in self.apps:
            if app['title'] == page:
                app['function']()
                break
