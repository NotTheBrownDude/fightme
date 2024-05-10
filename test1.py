import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit app title
st.title("Roller Coaster Data")
# Read the CSV file into a DataFrame
df = pd.read_csv(r"rollercoaster data.csv")
st.dataframe(df)

data_counts = df["Type"].value_counts()
fig, ax = plt.subplots()
ax.pie(data_counts, labels=data_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)


data_counts = df['Design'].value_counts()
plt.figure(figsize=(10, 6))  # Adjust figure size if needed
data_counts.plot(kind='bar', rot=45)  # Create bar chart with rotated x-axis labels
plt.xlabel('Design')
plt.ylabel('Count')
plt.title('Count of Each Design Type')
st.pyplot(plt)  # Display the bar chart using st.pyplot()