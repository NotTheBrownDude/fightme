import streamlit as st
import numpy as np
import pandas as pd

def main():
    st.title("Streamlit Charts Showcase")

    # Line Chart
    st.header("Line Chart")
    data_line = np.random.randn(20, 2)  # Random data for demonstration
    st.line_chart(data_line)

    # Bar Chart
    st.header("Bar Chart")
    data_bar = pd.DataFrame({
        "Category": ["A", "B", "C", "D"],
        "Values": [20, 30, 25, 35]
    })
    st.bar_chart(data_bar.set_index("Category"))

    # Area Chart
    st.header("Area Chart")
    data_area = np.random.rand(10, 3)
    st.area_chart(data_area)

    # Histogram
    st.header("Histogram")
    data_hist = np.random.randn(1000)
    st.hist(data_hist, bins=50)

    # Pie Chart
    st.header("Pie Chart")
    data_pie = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas"],
        "Quantity": [20, 15, 30]
    })
    st.write(data_pie.set_index("Fruit"))
    st.pyplot()

    # Scatter Plot
    st.header("Scatter Plot")
    data_scatter = pd.DataFrame({
        "X": np.random.rand(50),
        "Y": np.random.rand(50)
    })
    st.scatter_chart(data_scatter)

    # Map
    st.header("Map")
    data_map = pd.DataFrame({
        "lat": [40.7128, 34.0522, 37.7749],
        "lon": [-74.0060, -118.2437, -122.4194],
        "name": ["New York", "Los Angeles", "San Francisco"]
    })
    st.map(data_map)

    # DataFrame/Table
    st.header("DataFrame/Table")
    data_table = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35]
    })
    st.dataframe(data_table)

if __name__ == "__main__":
    main()
