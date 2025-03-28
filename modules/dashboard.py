import streamlit as st

def launch_dashboard(papers, summaries):
    st.title("AI Gen and RAG Bibliographic Review Assistant")
    st.markdown("### Articles Found and Abstracts")

    for paper, summary in zip(papers, summaries):
        st.subheader(paper['title'])
        st.text_area("Abstract", summary, height = 150)

    st.markdown("#### The tool allows you to view abstracts of scientific articles quickly and efficiently!")
