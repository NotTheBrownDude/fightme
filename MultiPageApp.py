import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def page_home():
    st.title("Welcome to the world population app")
    st.write("Page 1- Population densities")
    st.write("Page 2- Growth rates")
    st.write("Page 3- World population percentage")
    st.write("Page 4- Population desities pie chart")
    st.image(r"whats-world-population.jpg")
    
DATA_URL = r"world_population.csv"

#@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.columns = data.columns.str.lower()
    return data

data_load_state = st.text('Loading data...')
data = load_data(5)
data_load_state.text("Done! (using st.cache_data)")

def page_chart_1():
    st.title("Population Densities")
    st.line_chart(data, x="density", y="country", color="#ffaa00")

def page_chart_2():
    st.title("Growth Rates")
    st.bar_chart(data, x="country", y="growth rate", color="#ffaa00")

def page_chart_3():
    st.title("World Population Percentage")
    st.bar_chart(data, x="country", y="world population percentage", color="#ffaa00")

def autopct_values(pct, allvalues):
        absolute = int(pct/100.*sum(allvalues))
        return f"{absolute:.1f}"

def page_chart_4():
    st.title("Population Desities Pie Chart")
    labels = ["Afghanistan", "Albania", "Algeria", "American Samoa"]
    densities = [63.0587, 98.8702, 18.8531, 222.4774]
    colors = ["#ff9999","#66b3ff","#99ff99","#ffcc99"]
    explode = (0, 0, 0, 0.2)  # explode the 1st slice (Afghanistan)
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(densities, explode=explode, labels=labels, colors=colors, autopct=lambda pct: f"{(pct/100)*sum(densities):.1f}", shadow=True, startangle=140)

    for autotext in autotexts:
        autotext.set_color('black')

    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display the pie chart in Streamlit
    st.pyplot(fig)



pages = {
    "Home": page_home,
    "Population Densities": page_chart_1,
    "Growth Rates": page_chart_2,
    "World Population %": page_chart_3,
    "Population Desities": page_chart_4
}

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", list(pages.keys()))
    pages[page]()

if __name__ == "__main__":
    main()


#####look at all the different charts and see which will suit the last two pages best~~~ all charts on test2