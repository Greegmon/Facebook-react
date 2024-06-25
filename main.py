import streamlit as st
import json

app = ["Second", "Third", "Fourth"]
with open('test.json', 'r') as fl:
	data = json.load(fl)

for _ in app:
	data['msg'].append(_)

with open('test.json', 'w') as op:
	json.dump(data, op, indent=2)

st.code(data)
