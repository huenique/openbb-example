import st_pages

st_pages.add_page_title()  # type: ignore

st_pages.show_pages(  # type: ignore
    [
        st_pages.Page("openbb_example/home.py", "Home", "🏠"),
        st_pages.Page("openbb_example/openbb_gpt.py", "OpenBB-GPT", "🦋"),
        st_pages.Page("openbb_example/pages/crypto_onchain.py", "Onchain Crypto", "📈"),
        st_pages.Page("openbb_example/pages/dark_pool.py", "Dark Pool Activity", "🌘"),
        st_pages.Page(
            "openbb_example/pages/gov_contracts.py", "Government Activity", "🗳️"
        ),
        st_pages.Page("openbb_example/pages/mutual_funds.py", "Economy Analysis", "📈"),
        st_pages.Page(
            "openbb_example/pages/options_analysis_gpt.py", "Options Analysis", "📈"
        ),
        st_pages.Page("openbb_example/pages/pdf_gpt.py", "PDF Analysis", "📈"),
        st_pages.Page(
            "openbb_example/pages/sentiment_analysis.py", "Sentiment Analysis", "📈"
        ),
    ]
)
