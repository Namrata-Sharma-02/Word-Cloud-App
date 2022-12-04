''' This app is used to get a URL from user and display the word cloud 
This app used to shoe the capabiltity of web scrapping from a static website
Process the Text and generate the Word CLoud based on the frequency of the word. Bigger the size of the word , more frequently the word is used on that webpage
This App  is also my encounter with StreamLit exploration
'''
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import requests
from bs4 import BeautifulSoup


usr_url = ""

st.title("My First Word Cloud")
usr_url = st.text_input("Enter the URL", value="")
page = requests.get(usr_url)
soup = BeautifulSoup(page.content,"html.parser")

#Getting all the elemnts with heading "p" to parse
job_elements = soup.find_all("p")

#creating one string cariable to store all the text
my_string = ""
for item in job_elements:
    my_string = my_string + " "+item.text

#generating the word cloud 
word_cloud = WordCloud(collocations = False, background_color = 'white').generate(my_string)
fig, ax = plt.subplots()
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.rcParams["figure.figsize"] = (15,15)
plt.show()

#Displaying the word cloud using streamlit app
st.pyplot(fig)

