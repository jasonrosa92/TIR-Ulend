import streamlit as st
import pandas as pd
import numpy as npf

from apps.investments import investments
from apps.installments import installments


titles = {
    'TIR': "Taxa Interna de Retorno"
}

def sorting_dates_investments():    
    df = pd.DataFrame(investments)
    df ['created_at'] = pd.to_datetime(df['created_at'])
    df_ordenado = df.sort_values(by='created_at')
    return df_ordenado

def sorting_dates_installments():
    df = pd.DataFrame(installments)
    df ['due_date'] = pd.to_datetime(df['due_date'])
    df_ordenado = df.sort_values(by='due_date')  
    return df_ordenado
    
    
def data(investments, installments):
    day = []
    values = []
    
    for investment in investments:
        day.append(investment['created_at'])
        amount = investment['amount'].replace('.', '')
        values.append(-int(amount))        
    
    for installment in installments:
        day.append(input['created_at'])
        amount = installment['amount'].replace('.', '')
        values.append(amount)        

    dictionary_info = {
        'day' : day,
        'values' : values
    }
    return dictionary_info

def process_data_frame(dictionary_info):
    df = pd.DataFrame(dictionary_info)
    df ['day'] = pd.to_datetime(df['day'])
    full_dates = pd.date_range(df['day'].min(), df['day'].max(), freq='d')
    df_index = pd.DataFrame({'day': full_dates})
    df_index = df_index.merge(df, on='date', how='left').fillna(0)
    df_index = df_index.groupby('date').sum().reset_index()
    df_index['full'] = df_index['amount'].cumsum()
    return df_index

def TIR(df):
    irr = round(100 * npf.irr(df['amount']), 2)
    print(f"TIR: {irr}%")
    
def app():
    st.title("Cálculo Taxa Interna de Retorno")    
    df_investments = pd.DataFrame(sorting_dates_investments())
    df_installments = pd.DataFrame(sorting_dates_installments())
    st.write(df_investments, df_installments)
    
    dictionary_info = data(investments, installments)
    df_irr = process_data_frame(dictionary_info)    
    df_irr(TIR)
        
