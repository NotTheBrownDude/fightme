import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Rollercoasters around the World')

DATA_URL = r"C:\temp\rollercoaster data.csv"

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.columns = data.columns.str.lower()
    return data

data_load_state = st.text('Loading data...')
data = load_data(5)
data_load_state.text("Done! (using st.cache_data)")

NaC = ["amusement park", "type", "design", "status", "opened", "region", "country", "make", "speed (mph)"]


if st.checkbox('Show Ride Names and Cities'):
    data_filtered = data.drop(columns=NaC)
    st.subheader('Ride Names and Cities')
    st.write(data_filtered)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader('Number of Rollercoasters by Country')
rollercoasters_by_country = data['country'].value_counts()
st.bar_chart(rollercoasters_by_country)

####    START OF LINE CHART   ######
#speedNyear = ["name", "amusement park", "type", "design", "status", "city", "region", "country", "make"]
df = pd.DataFrame(data)
df['opened'] = pd.to_datetime(df['opened'])

# Set 'Date' column as the index (required for plotting time series)
df.set_index('opened', inplace=True)

# Plotting the line chart using Matplotlib
#st.title('Speed Over Time')
#st.line_chart(df)
####    END OF LINE CHART   ######

# Alternatively, you can use Matplotlib directly for more customization
fig, ax = plt.subplots()
ax.plot(df.index, df['speed (mph)'], marker='o', linestyle='-', color='r')
ax.set_title('Speed Over Time')
ax.set_xlabel('Year Opened')
ax.set_ylabel('Speed (mph)')
ax.grid(True)

# Display the Matplotlib plot using Streamlit
st.pyplot(fig)
