from datetime import datetime

import streamlit as st
import pandas as pd
import numpy as np

from apps.investments import investments
# from installments import installments

cashflow = {}

titles = {
    'TIR': "Taxa Interna de Retorno"
}

def sorting_dates(inverted_order):
    """
    Function responsible for sorting cash flow dates
    """
    
    #initial_date
    start_date = min(cashflow, key=lambda x: datetime.strptime(x, "%Y-%m-%d"))
    #final_date
    end_date = max(cashflow, key=lambda x: datetime.strptime(x, "%Y-%m-%d"))

    if inverted_order:
        io = pd.date_range(start=start_date, end=end_date)[::-1]
    else:
        io = pd.date_range(start=start_date, end=end_date)

    result = {}
    for value in io:
        result[value.strftime("%Y-%m-%d")] = 0.0

    for key, value in cashflow.items():
        result[key] = value

    return result

def append_values(data):
    """
    Function responsible for adding up the values of the same date
    """
    
    for value in data:
        try:
            cashflow[value['due_date']]
    

def app():
    st.title("Cálculo Taxa Interna de Retorno")
    project1_cf = pd.DataFrame({"Year":np.arange(0,6),
        "cf": [-800,200,250,300,350,400]})
    project2_cf = pd.DataFrame({"Year":np.arange(0,6),
        "cf": [-500,150,170,178,250,300]})
    st.write(project1_cf)
    irr1 = np.irr(project1_cf["cf"])
    irr2 = np.irr(project2_cf["cf"])
    irr_df = pd.DataFrame({"Name":["Project1", "Project2"],
                      "IRR":[irr1, irr2]})    
    st.write(irr_df)
    
