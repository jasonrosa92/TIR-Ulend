# -*- coding: utf-8 -*-
import streamlit as st
from apps import *


st.set_page_config(page_title='Teste Ulend')

st.sidebar.markdown("Teste Ulend")

opt = st.sidebar.selectbox("Taxa Interna de Retorno",
    options=[
        "TIR",
    ]
)

if opt == "TIR":
    tir()
else:
    pass