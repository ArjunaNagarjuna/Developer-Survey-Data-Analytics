import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Developer Survey Analysis", layout="wide")
st.title("📊 Developer Survey Data Explorer")

# Upload CSV files
data_file = st.file_uploader("Upload survey_results_public.csv", type="csv")
schema_file = st.file_uploader("Upload survey_results_schema.csv", type="csv")

if data_file and schema_file:
    data = pd.read_csv(data_file)
    schema = pd.read_csv(schema_file, index_col='qname')

    st.success("Files uploaded successfully!")

    # Preview
    st.subheader("🔍 Dataset Preview")
    st.dataframe(data.head())

    st.subheader("📖 Schema Preview")
    st.dataframe(schema.head())

    # Developer Types
    if "DevType" in data.columns:
        dev_types = data["DevType"].dropna().str.split(";").explode()
        dev_counts = dev_types.value_counts().head(10)
        st.subheader("👨‍💻 Top Developer Types")
        fig, ax = plt.subplots()
        dev_counts.plot(kind="bar", ax=ax)
        ax.set_ylabel("Count")
        ax.set_title("Top 10 Developer Types")
        st.pyplot(fig)

    # Education Level Distribution
    if "EdLevel" in data.columns:
        st.subheader("🎓 Education Level Distribution")
        percent_spread = data['EdLevel'].value_counts(normalize=True) * 100
        percent_spread = percent_spread.sort_values()
        fig, ax = plt.subplots()
        percent_spread.plot(kind='barh', ax=ax)
        ax.set_xlabel("Percentage")
        ax.set_ylabel("Education Level")
        ax.set_title("Distribution of Education Levels")
        st.pyplot(fig)

    # Learning Methods
    if "LearnCode" in data.columns:
        st.subheader("📚 Learning Methods")
        learn_methods = data['LearnCode'].dropna().str.split(";").explode()
        method_counts = learn_methods.value_counts()
        method_percentage = (method_counts / len(data)) * 100
        method_percentage = method_percentage.sort_values()
        fig, ax = plt.subplots()
        method_percentage.plot(kind='barh', ax=ax)
        for index, value in enumerate(method_percentage):
            ax.text(value, index, f'{value:.2f}%', va='center')
        st.pyplot(fig)

    # Online Platforms
    if "LearnCodeCoursesCert" in data.columns:
        st.subheader("🌐 Online Platforms")
        online_platform_responses = data[data['LearnCodeCoursesCert'].notna()]
        response_count = online_platform_responses['LearnCodeCoursesCert'].count()
        online_platform = data['LearnCodeCoursesCert'].dropna().str.split(";").explode()
        online_platform_counts = online_platform.value_counts()
        online_platform_percentage = (online_platform_counts / response_count) * 100
        online_platform_percentage = online_platform_percentage.sort_values()
        fig, ax = plt.subplots()
        online_platform_percentage.plot(kind='barh', ax=ax)
        for index, value in enumerate(online_platform_percentage):
            ax.text(value, index, f'{value:.2f}%', va='center')
        st.pyplot(fig)

else:
    st.info("👆 Please upload both CSV files to begin.")
