import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Streamlit Practice Dashboard")

uploaded_file = st.file_uploader("Choose a csv file", type="csv")

if uploaded_file is not None:
    st.write("File uploaded")
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df.head(10))
    st.subheader("Data Summary")
    st.write(df.describe())
    st.subheader("Filtered Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_columns].unique()
    selected_values = st.selectbox("Select values",unique_values)
    filtered_df = df[df[selected_columns] == selected_values]
    st.write(filtered_df)
    st.subheader("Plot Data")
    x_column = st.selectbox("Select X axis column", columns)
    y_column = st.selectbox("Select Y axis column", columns)
    if st.button("Generate Chart"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Waiting on file upload")