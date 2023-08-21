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

st.title("Economy Analysis with OpenBB:butterfly: & ChatGPT:robot_face:")

choice = st.selectbox(
    label="Choose an Option based on today's Open Interest",
    options=(
        "Vanguard",
        "Capital",
        "BlackRock",
        "Morningstar",
        "Invesco",
        "Fidelity",
        "Goldman Sachs",
        "Value Line",
        "HSBC",
        "PRBLX",
        "SSAQX",
        "USBOX",
    ),
)

dat = openbb.funds.load(choice)
cont = st.container()

with cont:

    @st.cache_data(experimental_allow_widgets=True)
    def data_stream():
        st.write("Choose a Dataset to load")  # type: ignore

        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

        if "data" not in st.session_state:
            st.session_state["data"] = openbb.funds.carbon(dat)

        if col1.button("Carbon Metrics"):
            st.session_state["data"] = openbb.funds.carbon(dat)

        if col2.button("Exclusion Policy"):
            st.session_state["data"] = openbb.funds.exclusion(dat)

        if col3.button("Historical Performance"):
            st.session_state["data"] = openbb.funds.historical(
                dat, start_date="2020-01-01", end_date="2023-06-31"
            )

        if col4.button("Holdings"):
            st.session_state["data"] = openbb.funds.holdings(dat)

        if col5.button("Sector Data"):
            st.session_state["data"] = openbb.funds.sector(dat)


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

prompt_template = "{input}"
prompt = PromptTemplate(input_variables=["input"], template=prompt_template)
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
