import streamlit as st
st.title('Challenge Steamlit Romain J')

import pandas as pd
st.write("A partir du dataset des voitures, tu afficheras : ")
st.header("1 .une analyse de corrélation et de distribution grâce à différents graphiques et des commentaires ")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)
df_car

import seaborn as sns
import matplotlib.pyplot as plt

viz_correlation = sns.heatmap(df_car.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)
plt.title('Correlation Analysis of the Cars Dataset')
st.pyplot(viz_correlation.figure)
st.markdown("Comment 1 : mpg have a positive correlation with time-to60 & year")
st.markdown("Comment 2 : mpg have a negative correlation with cylinders, cubinches,hp and weightlbs")


st.header("2 .des boutons doivent être présents pour pouvoir filtrer les résultats par région (US / Europe / Japon). ")

subset_data = df_car
country_name_input = st.radio('Choose your country',
df_car.groupby('continent').count().reset_index()['continent'].tolist())
# by country name
if len(country_name_input) >= 0:
    subset_data = df_car[df_car['continent']==country_name_input]
distribution = sns.displot(subset_data, x="mpg")
plt.title('Distribution of mpg per country')
st.pyplot(distribution.figure)   

st.markdown("Comment 1 : There are more cars in the US than Europe & Japan")

st.markdown("![wait for it](https://media.giphy.com/media/g0pZt4jizASYVkRPRi/giphy-downsized-large.gif)")


#display the module version for requirement.txt purpose
st.write("streamlit==",st.__version__)
st.write("pandas==",pd.__version__)
st.write("seaborn==",sns.__version__)