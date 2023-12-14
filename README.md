# Customer Data Analysis with Streamlit

This project analyzes customer data using Streamlit, a powerful Python library for creating web applications with interactive visualizations. The analysis includes exploratory data analysis (EDA) and provides users with the flexibility to input custom SQL queries.

## Overview

The application allows users to upload a CSV file containing customer data. It provides various visualizations and insights into the dataset, including:

- Displaying column names and types.
- Showing the first 10 rows of the dataset.
- Age distribution with a histogram.
- Gender distribution with a count plot.
- Age distribution by gender with a box plot.
- Pie chart for profession distribution.
- Bar chart for annual income distribution.
- Scatter plot for age vs spending score.

Users can also input their custom SQL queries to explore the dataset further.

## How to Use

1. **Upload CSV File:** Use the "Upload a CSV file" section to upload your customer dataset in CSV format.

2. **Exploratory Data Analysis (EDA):** Explore various visualizations and insights provided by the app.

3. **Custom Queries:** Input your custom SQL queries in the "Custom Queries" section to perform specific analyses on the dataset.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/customer-data-analysis.git
   ```

2. Navigate to the project directory:

   ```bash
   cd customer-data-analysis
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

The application will open in your default web browser.

## Dependencies

- [Streamlit](https://www.streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

## Contributing

If you have suggestions or find issues, feel free to open an issue or submit a pull request.
