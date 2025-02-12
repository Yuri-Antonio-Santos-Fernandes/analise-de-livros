#novas pastas = novas paginas no arquivo
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


df_reviews = pd.read_csv("dateassets/customer reviews.csv")
df_top100 = pd.read_csv("dateassets/Top-100 Trending Books.csv")

#garante que não ocorra repetição dos titulos
books = df_top100["book title"].unique()

#cria uma caixa de seleção de titulos
book = st.sidebar.selectbox("books", books)

#garante que sempre que eu selecionar um titulo somente ele apareça para mim com suas informações
df_book = df_top100[df_top100["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

#faz com que somente certos dados sejam mostrados ao invez de tudo
book_title = df_book["book title"].iloc[0]
book_price = df_book["book price"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_rating = df_book["rating"].iloc[0]
book_publication = df_book["year of publication"].iloc[0]

#concede titulo e subtitulo
st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)

col1.metric("$", book_price)
col2.metric("rating", book_rating)
col3.metric("publication", book_publication)

st.divider()

for row in df_reviews_f.values:
     m = st.chat_message(f"{row[4]}")
     m.write(f"{row[2]}")
     m.write(f"{row[5]}")