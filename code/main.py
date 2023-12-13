import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

# Set up matplotlib style
plt.style.use('fivethirtyeight')

st.title("Customer Data Analysis")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV data
    customer_data = pd.read_csv(uploaded_file)

    # Display column names and types
    st.subheader("Columns and Types:")
    st.dataframe(customer_data.dtypes.reset_index().rename(columns={0: 'Data Type', 'index': 'Column Name'}))

    # Exploratory Data Analysis (EDA)
    st.subheader("Exploratory Data Analysis (EDA):")

    # Display first 10 rows of the dataset
    st.subheader("First 10 Rows:")
    st.dataframe(customer_data.head(10))

    # Bar chart for age distribution
    st.subheader("Age Distribution:")
    plt.figure(figsize=(10, 6))
    sns.histplot(customer_data['Age'], bins=20, color='skyblue', edgecolor='black', kde=True)
    plt.title('Age Distribution of Customers')
    plt.xlabel('Age')
    plt.ylabel('Count')
    st.pyplot()

    # Count plot for gender distribution
    st.subheader("Gender Distribution:")
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Gender', data=customer_data, palette='pastel')
    plt.title('Gender Distribution of Customers')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    st.pyplot()

    # Box plot for age distribution by gender
    st.subheader("Age Distribution by Gender:")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Gender', y='Age', data=customer_data, palette='pastel')
    plt.title('Age Distribution by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Age')
    st.pyplot()

    # Pie chart for profession distribution
    st.subheader("Profession Distribution:")
    profession_counts = customer_data['Profession'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.pie(profession_counts, labels=profession_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Distribution of Professions')
    st.pyplot()

    # Bar chart for annual income distribution
    st.subheader("Annual Income Distribution:")
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Annual Income ($)', y='CustomerID', data=customer_data, palette='pastel')
    plt.title('Annual Income Distribution of Customers')
    plt.xlabel('Annual Income ($)')
    plt.ylabel('Count')
    st.pyplot()

    # Scatter plot for age vs spending score
    st.subheader("Age vs Spending Score:")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Age', y='Spending Score (1-100)', data=customer_data, hue='Gender', palette='pastel')
    plt.title('Age vs Spending Score')
    plt.xlabel('Age')
    plt.ylabel('Spending Score (1-100)')
    st.pyplot()

    # Summary statistics table
    st.subheader("Summary Statistics:")
    st.dataframe(customer_data.describe())
else:
    st.warning("Please upload a CSV file.")

