import sqlite3

import pandas as pd
import st_pages
import streamlit as st
from langchain import OpenAI, PromptTemplate, SQLDatabase
from langchain.callbacks import get_openai_callback
from langchain_experimental.sql import SQLDatabaseChain
from openbb_terminal.sdk import openbb
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

st_pages.add_page_title()  # type: ignore

st.title("Crypto Onchain data analysis with OpenBB:butterfly: & ChatGPT:robot_face:")

options_df = openbb.crypto.onchain.erc20_tokens()

choice = st.selectbox(label="Choose a Crypto", options=(options_df["symbol"]))

cont = st.container()

with cont:

    @st.cache_data(experimental_allow_widgets=True)
    def data_stream():
        st.write("Choose a Dataset to load")  # type: ignore

        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

        if "data" not in st.session_state:
            st.session_state["data"] = openbb.crypto.onchain.tv()

        if col1.button("Token Volume"):
            st.session_state["data"] = openbb.crypto.onchain.tv()

        if col2.button("DEX Trades"):
            st.session_state["data"] = openbb.crypto.onchain.lt()

        if col3.button("Daily Volumes"):
            st.session_state["data"] = openbb.crypto.onchain.dvcp(symbol=choice)

        if col4.button("Monthly DEX Trades"):
            st.session_state["data"] = openbb.crypto.onchain.dex_trades_monthly()

        if col5.button("Bid & Ask Prices"):
            st.session_state["data"] = openbb.crypto.onchain.baas(symbol=choice)


data_stream()

data1 = st.session_state["data"]
st.write(data1)  # type: ignore

table_name = "statesdb"
uri = "file:memory?cache=shared&mode=memory"
openai_key = st.secrets["OPENAI_KEY"]

query = st.text_input(
    label="Any questions?", help="Ask any question based on the loaded dataset"
)

conn = sqlite3.connect(uri, uri=True)

if isinstance(data1, pd.DataFrame):
    if not data1.empty:
        data1.to_sql(table_name, conn, if_exists="replace", index=False)
    else:
        st.write("No data")  # type: ignore

else:
    st.write("Error. Invalid data or failed API connection.")  # type: ignore

db_eng = create_engine(
    url="sqlite:///file:memdb1?mode=memory&cache=shared",
    poolclass=StaticPool,
    creator=lambda: conn,
)
db = SQLDatabase(engine=db_eng)

template = """You are an SQLite expert. Given an input question, first create a
syntactically correct SQLite query to run, then look at the results of the query and
return the answer to the input question. Unless the user specifies in the question a
specific number of examples to obtain, query for at most {top_k} results using the LIMIT
clause as per SQLite. You can order the results to return the most informative data in
the database. Never query for all columns from a table. You must query only the columns
that are needed to answer the question. Wrap each column name in double quotes (") to
denote them as delimited identifiers. Pay attention to use only the column names you
can see in the tables below. Be careful to not query for columns that do not exist.
Also, pay attention to which column is in which table.

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here

Only use the following tables:
{table_info}

Question: {input}
"""
prompt = PromptTemplate(input_variables=["input"], template=template)
lang_model = OpenAI(
    openai_api_key=openai_key,
    temperature=0.9,
    max_tokens=300,
    client=None,
)
db_chain = SQLDatabaseChain.from_llm(  # type: ignore
    llm=lang_model,
    db=db,
    prompt=prompt,
)

if query:
    with get_openai_callback() as cb:
        response = db_chain.run(query)
        st.sidebar.write(  # type: ignore
            f"Your request costs: {str(cb.total_cost)} USD"
        )
    st.write(response)  # type: ignore
