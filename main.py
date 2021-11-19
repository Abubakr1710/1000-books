from logging import PlaceHolder
from altair.vegalite.v4.schema.channels import Size
from altair.vegalite.v4.schema.core import Align
from matplotlib.pyplot import margins, title
from pandas.io.stata import stata_epoch
import streamlit as st
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()
interactive = st.beta_container()
The_end = st.beta_container()

st.markdown(
"""
<style>
.main{
    background-color: #F5F5F5;
}
</style>
""",
unsafe_allow_html = True
)

background_color = '#F5F5F5'


with header:
    st.title('Web Scraping & Analysis')
    st.text('Need to scrape data from goodreads.com')


with dataset:
    st.header('Scraping')
    st.text('Scraping the information of the first 1000 books using BeautifulSoup and requests')
    st.text('The data scrap from multiple pages')
   
    
    data = pd.read_csv('C:/Users/Abu/Desktop/streamlitgo/my_data.csv', sep='&')
    st.write(data)
with features:
    st.header('Pandas')
    st.subheader('Pandas converted the data into a DataFrame')
    if st.checkbox('Show Center Information data'):
        st.subheader('Center Information data')
        st.write(data)


with model_training:
    st.header('Time to Data Analysis!!!')


with interactive:
    st.title('A closer look into the data')

    fig = go.Figure(data = go.Table(
        columnwidth = [2, 2, 1, 1, 1, 1, 1, 4, 1, 1, 1, 3],
        header = dict(values = list(data[['Title', 'author','num_reviews', 'num_ratings', 'avg_rating', 'Publication_year', 'Series', 'genres', 'Awards', 'places', 'Rating', 'mean_norm_rating' ]].columns),
            fill_color = '#FD8E72',
            align = 'center'),
        cells = dict(values = [data.Title, data.author, data.num_reviews, data.num_ratings, data.avg_rating, data.Publication_year, data.Series, data.genres, data.Awards, data.places, data.Rating, data.mean_norm_rating],
            fill_color = '#E5ECF6',
            align = 'left' )))

    fig.update_layout(margin = dict(l=5, r=5, b=10, t=10),
    paper_bgcolor = background_color)

    st.write(fig)        

    st.subheader('The bar graph illustrates published books from 1999 to 2019')

    States = pd.DataFrame(data['Publication_year'].value_counts()).head(20)
    st.bar_chart(States)

    st.subheader('The bar graph shows the most twenty Average Rating')
    States = pd.DataFrame(data['avg_rating'].value_counts()).head(20)
    st.bar_chart(States)

    st.subheader('The bar graph represent number of books published from 1999 to 2019 ')
    States = pd.DataFrame(data['Publication_year'].value_counts()).head(20)
    st.bar_chart(States)

chart_select = st.sidebar.selectbox(
    label="select the chart type",
    options=['scatterplots','lineplots','Histogram','Boxplot']
)


with The_end:
    st.markdown('* **Thank you very much**')
    st.title('GROUP MEMBERS:')
    st.text('VENATI HIMANTH')
    st.text('HARI KISHORE')
    st.text('ABUBAKR MAMAJONOV')
    
    
    