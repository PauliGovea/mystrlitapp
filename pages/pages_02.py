import requests

import streamlit as st

import numpy as np


st.set_page_config(page_title="Hello", page_icon="🤟🏼")


st.markdown("# Streamlit is awesome! 👾")


if st.button("click ;)"):
    st. image ("raw_data/enterprise.png")


query = st.text_input("Day of the week")
url = "https://my-api-3gsawzgwlq-ew.a.run.app"
params = {"day_of_week": query, "time": 10}
response = requests.get(url=url, params=params)

while not query:
    st.stop()

st.write(response.json())
