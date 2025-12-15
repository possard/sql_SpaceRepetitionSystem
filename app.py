import streamlit as st
import pandas as pd
import duckdb


st.write("Interpréteur SQL + Examples de présentation:")
data = {"a": [1,2,3],"b": [4,5,6],"c": [7,8,9]}
df = pd.DataFrame(data)

tab0, tab1, tab2, tab3 = st.tabs(["SQL","Chats","Chiens","Hiboux"])

with tab0:
    st.write("Interpréteur SQL")
    sql_query = st.text_area(label="Entrez votre requête SQL:")
    st.write(f"Vous avez entré la requete suivante: {sql_query}")

    if len(sql_query)>0:
        result = duckdb.sql(sql_query).df()
        st.dataframe(result)

with tab1:
    st.write("Chats")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.write("Chien")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.write("Hibou")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
