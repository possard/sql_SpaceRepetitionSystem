# pylint: disable=missing-module-docstring
import io

import duckdb
import pandas as pd
import streamlit as st

CSV = """
beverage,price
orange juice, 2.5
Expresso, 2
Tea, 3
"""
beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_price
cookie juice, 2.5
chocolatine, 2
muffin, 3
"""
food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_DF = """
SELECT * FROM beverages
CROSS JOIN food_items
"""
solution_df = duckdb.sql(ANSWER_DF).df()

with st.sidebar:
    option = st.selectbox(
        "Quels concepts voulez-vous réviser:",
        ("Joins", "Group By", "Windows functions"),
        index=None,
        placeholder="Choisissez un thème...",
    )

st.header("Enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.write(f"Votre requete: {query}")
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(solution_df.compare(result))
    except KeyError as e:
        st.write(f"Il vous manque des colonnes:  <{e}>")

    delta_nb_line = result.shape[0] - solution_df.shape[0]
    if delta_nb_line != 0:
        st.write(
            f"Vous n'avez pas le bon nombre de lignes que dans la solution:"
            f" {delta_nb_line} lignes de différence"
        )

tab2, tab3 = st.tabs(["Tables", "Solutions"])
with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution_df)

with tab3:
    st.write(ANSWER_DF)
    st.dataframe(solution_df)
