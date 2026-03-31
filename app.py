# -*- coding: utf-8 -*-
import streamlit as st
from markdown_pdf import MarkdownPdf, Section


def read_markdown_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def recipe_page(path:str, recipe:str):
    page_content = read_markdown_file(path)

    st.markdown(page_content)
    pdf = MarkdownPdf()
    pdf.meta["title"] = recipe
    pdf.add_section(Section(page_content, toc=False))
    pdf.save(f'pdfs/{recipe}.pdf')
    with open(f'pdfs/{recipe}.pdf', mode='rb') as f:
        st.download_button("Download Recipe", data=f, file_name=f"{recipe}.pdf", icon=":material/download:")

def home():
    
    st.title("Breakfast with the Circle")

    st.write("Welcome to the Circle breakfast! If you would like to find any of the recipes that were used by or members or other suggestions for recipes from our countries, feel free to have a look and even download a copy to use later. We hope you enjoy!")



pg = st.navigation([
    st.Page(home, title="Home", icon=":material/home:", default=True),
    st.Page("recipes/canada/canada.py", title="Canada"),
    st.Page("recipes/czechia/czechia.py", title="Czech Republic"),
    st.Page("recipes/france/france.py", title="France"),
    st.Page("recipes/luxembourg/luxembourg.py", title="Luxembourg"),
    st.Page("recipes/mexico/mexico.py", title="Mexico"),
    st.Page("recipes/netherlands/netherlands.py", title="Netherlands"),
    st.Page("recipes/turkey/turkey.py", title="Turkey")
])

pg.run()



