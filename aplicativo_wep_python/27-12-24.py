import streamlit as st
import pandas as pd
import plotly.express as px

#define a aparência da pagina.
st.set_page_config(layout="wide")

#salva os arquivos.csv de top 100 livros e reviews como variaveis que podem ser chamadas.
df_reviews = pd.read_csv("dateassets/customer reviews.csv")
df_top100 = pd.read_csv("dateassets/Top-100 Trending Books.csv")

#grava na variavel o maior valor no custo dos livros
price_max = df_top100["book price"].max()

#grava na variavel o menor valor no custo dos livros
price_min = df_top100["book price"].min()

#variavel do meu slider que vai servir para filtrar preços e a sidebar para criar uma barra lateral
slider = st.sidebar.slider("seletor de preço", price_min, price_max, price_max)

#chamando as variaveis.
st.title("top 100 mais vendidos")

#garantindo que o slider faça seu trabalho filtrando preços, mostrando somente os preços menores ou igual ao seu valor
df_books = df_top100[df_top100["book price"] <= slider]
df_books

#criação de um grafico de barras, primeiramente criando a variavel referente a ele
#depois setando que ele mostre os valores referentes aos anos de publicação dos livros
fig1 = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

#configurando o numero de colunas que eu quero
col1, col2 = st.columns(2)

#chamando meu grafico
#e chamando eles em linhas iguais mais em diferentes colunas
col1.plotly_chart(fig1)
col2.plotly_chart(fig2)
