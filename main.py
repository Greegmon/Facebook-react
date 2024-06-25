import streamlit as st
import json

app = ["Second", "Third", "Fourth"]
with open('test.json', 'r') as fl:
	data = json.load(fl)

oi = 0
u = False
if not u:
	data['msg'].append(app)
	u = True
	oi += 1

with open('test.json', 'w') as op:
	json.dump(data, op, indent=2)

st.write(oi)
st.write(u)
st.code(data)
