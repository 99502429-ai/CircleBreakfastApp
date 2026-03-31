# -*- coding: utf-8 -*-
import streamlit as st
from markdown_pdf import MarkdownPdf, Section



def read_markdown_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

path = "recipes/czechia/pernik.md"
recipe = "Pernik"

page_content = read_markdown_file(path)

st.markdown(page_content)
pdf = MarkdownPdf()
pdf.meta["title"] = recipe
pdf.add_section(Section(page_content, toc=False))
pdf.save(f'pdfs/{recipe}.pdf')
with open(f'pdfs/{recipe}.pdf', mode='rb') as f:
    st.download_button("Download Recipe", data=f, file_name=f"{recipe}.pdf", icon=":material/download:")






