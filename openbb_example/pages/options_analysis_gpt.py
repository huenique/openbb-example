import sqlite3
from datetime import datetime

import st_pages
import streamlit as st
from dateutil.relativedelta import relativedelta
from langchain import OpenAI, PromptTemplate, SQLDatabase
from langchain.callbacks import get_openai_callback
from langchain_experimental.sql import SQLDatabaseChain
from openbb_terminal.sdk import openbb
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

st_pages.add_page_title()  # type: ignore

st.title("Options Analysis with OpenBB:butterfly: & ChatGPT:robot_face:")

unu_df, unu_ts = openbb.stocks.options.unu(limit=500)

unu_df = unu_df.sort_values(by="Vol/OI", ascending=False)
choice = st.selectbox(
    label="Choose an Option based on today's Open Interest", options=(unu_df["Ticker"])
)

cont = st.container()

with cont:

    @st.cache_data(experimental_allow_widgets=True)
    def data_stream():
        st.write("Choose a Dataset to load for your Stock Option")  # type: ignore

        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
        _expiry = datetime.today() + relativedelta(months=1)

        if "data" not in st.session_state:
            st.session_state["data"] = openbb.stocks.options.info(choice)

        if col1.button("Put-Call Ratio"):
            st.session_state["data"] = openbb.stocks.options.pcr(choice)

        if col2.button("Options Info"):
            st.session_state["data"] = openbb.stocks.options.info(choice)

        if col3.button("Options Chains"):
            st.session_state["data"] = openbb.stocks.options.chains(choice)

        if col4.button(
            "EOD Chain", help="Requires Intrinio API Key :closed_lock_with_key:"
        ):
            st.session_state["data"] = openbb.stocks.options.eodchain(choice)

        if col5.button("Volatility Surface"):
            st.session_state["data"] = openbb.stocks.options.vsurf(choice)


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

data1.to_sql(table_name, conn, if_exists="replace", index=False)

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
