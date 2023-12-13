import streamlit as st
import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import seaborn as sns

# Create empty database
db_path = "Customer.db"
Path(db_path).touch()

# Connect to the database
conn = sqlite3.connect(db_path)

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE IF NOT EXISTS customer (
    CustomerID INTEGER, 
    Gender TEXT,
    Age INTEGER, 
    "Annual Income ($)" INTEGER,
    "Spending Score (1-100)" INTEGER,
    Profession TEXT, 
    "Work Experience" INTEGER,
    "Family Size" INTEGER
    );"""
)

# Open csv file
customer_data = pd.read_csv("/home/vignesh-nadar/vikky/projects/ML/project 1/Customer Segmentation application using SQL/Customers.csv")

# Add data to the table
customer_data.to_sql("customer", conn, if_exists="replace", index=False)

# Display column names and types
query = "PRAGMA table_info(customer);"
columns_info = pd.read_sql_query(query, conn)

# Streamlit app starts here
st.title("Customer Data Analysis")

# Display column names and types
st.subheader("Columns and Types:")
st.text("""
        CustomerID(INTEGER)	
        Gender(TEXT) Age(INTEGER)
        Annual Income ($)(INTEGER)
        Spending Score (1-100)(INTEGER)
        Profession(TEXT)
        Work Experience(INTEGER)
        Family Size(INTEGER)
        """)

#print("Columns and Types: CustomerID(INTEGER)	Gender(TEXT) Age(INTEGER)	Annual Income ($)(INTEGER)	Spending Score (1-100)(INTEGER)	Profession(TEXT)	Work Experience(INTEGER)	Family Size(INTEGER)")
#print(tabulate(columns_info, headers='keys', tablefmt='pretty'))

# Take user input for SQL query
user_query = st.text_input("Enter your SQL query: ")

# Execute user's SQL query
try:
    if user_query:  # Check if user_query is not empty
        result = pd.read_sql_query(user_query, conn)
        st.subheader("Query Result:")
        st.dataframe(result)

        # Visualization: Plot correlation for multiple columns
        if len(result.columns) > 1:
            st.subheader("Correlation Plot:")
            sns.pairplot(result)
            st.pyplot()
            st.set_option('deprecation.showPyplotGlobalUse', False)
        # Visualization: Simple bar chart for age distribution
        #if 'Age' in result.columns:
        #    st.subheader("Age Distribution of Customers:")
        #    plt.figure(figsize=(10, 6))
        #    plt.hist(result['Age'], bins=20, color='skyblue', edgecolor='black')
        #    plt.title('Age Distribution of Customers')
        #    plt.xlabel('Age')
        #    plt.ylabel('Count')
        #    st.pyplot(plt)
except Exception as e:
    st.error(f"Error executing query: {e}")


# Close the connection
conn.close()
