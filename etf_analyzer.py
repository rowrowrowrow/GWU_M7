#!/usr/bin/env python
# coding: utf-8

# # Create a Web Application for an ETF Analyzer
# 
# In this Challenge assignment, you’ll build a financial database and web application by using SQL, Python, and the Voilà library to analyze the performance of a hypothetical fintech ETF.
# 
# Instructions: 
# 
# Use this notebook to complete your analysis of a fintech ETF that consists of four stocks: GOST, GS, PYPL, and SQ. Each stock has its own table in the `etf.db` database, which the `Starter_Code` folder also contains.
# 
# Analyze the daily returns of the ETF stocks both individually and as a whole. Then deploy the visualizations to a web application by using the Voilà library.
# 
# The detailed instructions are divided into the following parts:
# 
# * Analyze a single asset in the ETF
# 
# * Optimize data access with Advanced SQL queries
# 
# * Analyze the ETF portfolio
# 
# * Deploy the notebook as a web application
# 
# #### Analyze a Single Asset in the ETF
# 
# For this part of the assignment, you’ll use SQL queries with Python, Pandas, and hvPlot to analyze the performance of a single asset from the ETF.
# 
# Complete the following steps:
# 
# 1. Write a SQL `SELECT` statement by using an f-string that reads all the PYPL data from the database. Using the SQL `SELECT` statement, execute a query that reads the PYPL data from the database into a Pandas DataFrame.
# 
# 2. Use the `head` and `tail` functions to review the first five and the last five rows of the DataFrame. Make a note of the beginning and end dates that are available from this dataset. You’ll use this information to complete your analysis.
# 
# 3. Using hvPlot, create an interactive visualization for the PYPL daily returns. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.
# 
# 4. Using hvPlot, create an interactive visualization for the PYPL cumulative returns. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.
# 
# #### Optimize Data Access with Advanced SQL Queries
# 
# For this part of the assignment, you’ll continue to analyze a single asset (PYPL) from the ETF. You’ll use advanced SQL queries to optimize the efficiency of accessing data from the database.
# 
# Complete the following steps:
# 
# 1. Access the closing prices for PYPL that are greater than 200 by completing the following steps:
# 
#     - Write a SQL `SELECT` statement to select the dates where the PYPL closing price was higher than 200.0.
# 
#     - Using the SQL statement, read the data from the database into a Pandas DataFrame, and then review the resulting DataFrame.
# 
#     - Select the “time” and “close” columns for those dates where the closing price was higher than 200.0.
# 
# 2. Find the top 10 daily returns for PYPL by completing the following steps:
# 
#     -  Write a SQL statement to find the top 10 PYPL daily returns. Make sure to do the following:
# 
#         * Use `SELECT` to select only the “time” and “daily_returns” columns.
# 
#         * Use `ORDER` to sort the results in descending order by the “daily_returns” column.
# 
#         * Use `LIMIT` to limit the results to the top 10 daily return values.
# 
#     - Using the SQL statement, read the data from the database into a Pandas DataFrame, and then review the resulting DataFrame.
# 
# #### Analyze the ETF Portfolio
# 
# For this part of the assignment, you’ll build the entire ETF portfolio and then evaluate its performance. To do so, you’ll build the ETF portfolio by using SQL joins to combine all the data for each asset.
# 
# Complete the following steps:
# 
# 1. Write a SQL query to join each table in the portfolio into a single DataFrame. To do so, complete the following steps:
# 
#     - Use a SQL inner join to join each table on the “time” column. Access the “time” column in the `GDOT` table via the `GDOT.time` syntax. Access the “time” columns from the other tables via similar syntax.
# 
#     - Using the SQL query, read the data from the database into a Pandas DataFrame. Review the resulting DataFrame.
# 
# 2. Create a DataFrame that averages the “daily_returns” columns for all four assets. Review the resulting DataFrame.
# 
#     > **Hint** Assuming that this ETF contains equally weighted returns, you can average the returns for each asset to get the average returns of the portfolio. You can then use the average returns of the portfolio to calculate the annualized returns and the cumulative returns. For the calculation to get the average daily returns for the portfolio, use the following code:
#     >
#     > ```python
#     > etf_portfolio_returns = etf_portfolio['daily_returns'].mean(axis=1)
#     > ```
#     >
#     > You can use the average daily returns of the portfolio the same way that you used the daily returns of a single asset.
# 
# 3. Use the average daily returns in the `etf_portfolio_returns` DataFrame to calculate the annualized returns for the portfolio. Display the annualized return value of the ETF portfolio.
# 
# > **Hint**  To calculate the annualized returns, multiply the mean of the `etf_portfolio_returns` values by 252.
# >
# > To convert the decimal values to percentages, multiply the results by 100.
# 
# 4. Use the average daily returns in the `etf_portfolio_returns` DataFrame to calculate the cumulative returns of the ETF portfolio.
# 
# 5. Using hvPlot, create an interactive line plot that visualizes the cumulative return values of the ETF portfolio. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.
# 
# #### Deploy the Notebook as a Web Application
# 
# For this part of the assignment, complete the following steps:
# 
# 1. Use the Voilà library to deploy your notebook as a web application. You can deploy the web application locally on your computer.
# 
# 2. Take a screen recording or screenshots to show how the web application appears when using Voilà. Include the recording or screenshots in the `README.md` file for your GitHub repository.
# 

# ## Review the following code which imports the required libraries, initiates your SQLite database, popluates the database with records from the `etf.db` seed file that was included in your Starter_Code folder, creates the database engine, and confirms that data tables that it now contains.

# In[1]:


# Importing the required libraries and dependencies
import numpy as np
import pandas as pd
import hvplot.pandas
import sqlalchemy

# Create a temporary SQLite database and populate the database with content from the etf.db seed file
database_connection_string = 'sqlite:///etf.db'

# Create an engine to interact with the SQLite database
engine = sqlalchemy.create_engine(database_connection_string)

# Confirm that table names contained in the SQLite database.
table_names = engine.table_names()


# ## Analyze a single asset in the FinTech ETF
# 
# For this part of the assignment, you’ll use SQL queries with Python, Pandas, and hvPlot to analyze the performance of a single asset from the ETF.
# 
# Complete the following steps:
# 
# 1. Write a SQL `SELECT` statement by using an f-string that reads all the PYPL data from the database. Using the SQL `SELECT` statement, execute a query that reads the PYPL data from the database into a Pandas DataFrame.
# 
# 2. Use the `head` and `tail` functions to review the first five and the last five rows of the DataFrame. Make a note of the beginning and end dates that are available from this dataset. You’ll use this information to complete your analysis.
# 
# 3. Using hvPlot, create an interactive visualization for the PYPL daily returns. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.
# 
# 4. Using hvPlot, create an interactive visualization for the PYPL cumulative returns. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.
# 
# 

# ### Step 1: Write a SQL `SELECT` statement by using an f-string that reads all the PYPL data from the database. Using the SQL `SELECT` statement, execute a query that reads the PYPL data from the database into a Pandas DataFrame.

# In[2]:


# Write a SQL query to SELECT all of the data from the PYPL table
query = '''
SELECT *
FROM PYPL
'''

# Use the query to read the PYPL data into a Pandas DataFrame
pypl_dataframe = pd.read_sql_query(query, con=engine)
pypl_dataframe['time'] = pd.to_datetime(pypl_dataframe['time'])
pypl_dataframe.dtypes


# ### Step 2: Use the `head` and `tail` functions to review the first five and the last five rows of the DataFrame. Make a note of the beginning and end dates that are available from this dataset. You’ll use this information to complete your analysis.

# In[3]:


# View the first 5 rows of the DataFrame.
pypl_dataframe.head()


# In[4]:


# View the last 5 rows of the DataFrame.
pypl_dataframe.tail()


# ### Step 3: Using hvPlot, create an interactive visualization for the PYPL daily returns. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.

# In[5]:


# Create an interactive visualization with hvplot to plot the daily returns for PYPL.
pypl_dataframe_daily_returns_plot = pypl_dataframe.hvplot.line(
    title="PYPL Daily Returns",
    x="time",
    xlabel="Time",
    y="daily_returns",
    ylabel='Daily Returns',
    rot=90,
)

pypl_dataframe_daily_returns_plot


# ### Step 4: Using hvPlot, create an interactive visualization for the PYPL cumulative returns. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.

# In[6]:


# Create an interactive visaulization with hvplot to plot the cumulative returns for PYPL.
pypl_dataframe['cumulative_returns'] = (1 + pypl_dataframe['daily_returns']).cumprod()

pypl_dataframe_cumulative_returns_plot = pypl_dataframe.hvplot.line(
    title="PYPL Cumulative Returns",
    x="time",
    xlabel="Time",
    y="cumulative_returns",
    ylabel='Cumulative Returns',
    rot=90,
)

pypl_dataframe_cumulative_returns_plot


# ## Optimize the SQL Queries
# 
# For this part of the assignment, you’ll continue to analyze a single asset (PYPL) from the ETF. You’ll use advanced SQL queries to optimize the efficiency of accessing data from the database.
# 
# Complete the following steps:
# 
# 1. Access the closing prices for PYPL that are greater than 200 by completing the following steps:
# 
# 1. Access the closing prices for PYPL that are greater than 200 by completing the following steps:
# 
#     - Write a SQL `SELECT` statement to select the dates where the PYPL closing price was higher than 200.0.
# 
#     - Select the “time” and “close” columns for those dates where the closing price was higher than 200.0.
# 
#     - Using the SQL statement, read the data from the database into a Pandas DataFrame, and then review the resulting DataFrame.
# 
# 2. Find the top 10 daily returns for PYPL by completing the following steps:
# 
#     -  Write a SQL statement to find the top 10 PYPL daily returns. Make sure to do the following:
# 
#         * Use `SELECT` to select only the “time” and “daily_returns” columns.
# 
#         * Use `ORDER` to sort the results in descending order by the “daily_returns” column.
# 
#         * Use `LIMIT` to limit the results to the top 10 daily return values.
# 
#     - Using the SQL statement, read the data from the database into a Pandas DataFrame, and then review the resulting DataFrame.
# 

# ### Step 1: Access the closing prices for PYPL that are greater than 200 by completing the following steps:
# 
#     - Write a SQL `SELECT` statement to select the dates where the PYPL closing price was higher than 200.0.
# 
#     - Select the “time” and “close” columns for those dates where the closing price was higher than 200.0.
# 
#     - Using the SQL statement, read the data from the database into a Pandas DataFrame, and then review the resulting DataFrame.
# 

# In[7]:


# Write a SQL SELECT statement to select the time and close columns 
# where the PYPL closing price was higher than 200.0.
query = '''
SELECT time, close
FROM PYPL
WHERE PYPL.close > 200.0
'''

# Using the query, read the data from the database into a Pandas DataFrame
pypl_higher_than_200 = pd.read_sql_query(query, con=engine)

# Review the resulting DataFrame
pypl_higher_than_200


# ### Step 2: Find the top 10 daily returns for PYPL by completing the following steps:
# 
#     -  Write a SQL statement to find the top 10 PYPL daily returns. Make sure to do the following:
# 
#         * Use `SELECT` to select only the “time” and “daily_returns” columns.
# 
#         * Use `ORDER` to sort the results in descending order by the “daily_returns” column.
# 
#         * Use `LIMIT` to limit the results to the top 10 daily return values.
# 
#     - Using the SQL statement, read the data from the database into a Pandas DataFrame, and then review the resulting DataFrame.
# 

# In[8]:


# Write a SQL SELECT statement to select the time and daily_returns columns
# Sort the results in descending order and return only the top 10 return values
query = '''
SELECT time, daily_returns
FROM PYPL
ORDER BY PYPL.daily_returns DESC
LIMIT 10
'''

# Using the query, read the data from the database into a Pandas DataFrame
pypl_top_10_returns = pd.read_sql_query(query, con=engine)

# Review the resulting DataFrame
pypl_top_10_returns


# ## Analyze the Fintech ETF Portfolio
# 
# For this part of the assignment, you’ll build the entire ETF portfolio and then evaluate its performance. To do so, you’ll build the ETF portfolio by using SQL joins to combine all the data for each asset.
# 
# Complete the following steps:
# 
# 1. Write a SQL query to join each table in the portfolio into a single DataFrame. To do so, complete the following steps:
# 
#     - Use a SQL inner join to join each table on the “time” column. Access the “time” column in the `GDOT` table via the `GDOT.time` syntax. Access the “time” columns from the other tables via similar syntax.
# 
#     - Using the SQL query, read the data from the database into a Pandas DataFrame. Review the resulting DataFrame.
# 
# 2. Create a DataFrame that averages the “daily_returns” columns for all four assets. Review the resulting DataFrame.
# 
#     > **Hint** Assuming that this ETF contains equally weighted returns, you can average the returns for each asset to get the average returns of the portfolio. You can then use the average returns of the portfolio to calculate the annualized returns and the cumulative returns. For the calculation to get the average daily returns for the portfolio, use the following code:
#     >
#     > ```python
#     > etf_portfolio_returns = etf_portfolio['daily_returns'].mean(axis=1)
#     > ```
#     >
#     > You can use the average daily returns of the portfolio the same way that you used the daily returns of a single asset.
# 
# 3. Use the average daily returns in the `etf_portfolio_returns` DataFrame to calculate the annualized returns for the portfolio. Display the annualized return value of the ETF portfolio.
# 
# > **Hint**  To calculate the annualized returns, multiply the mean of the `etf_portfolio_returns` values by 252.
# >
# > To convert the decimal values to percentages, multiply the results by 100.
# 
# 4. Use the average daily returns in the `etf_portfolio_returns` DataFrame to calculate the cumulative returns of the ETF portfolio.
# 
# 5. Using hvPlot, create an interactive line plot that visualizes the cumulative return values of the ETF portfolio. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.
# 

# ### Step 1: Write a SQL query to join each table in the portfolio into a single DataFrame. To do so, complete the following steps:
# 
#     - Use a SQL inner join to join each table on the “time” column. Access the “time” column in the `GDOT` table via the `GDOT.time` syntax. Access the “time” columns from the other tables via similar syntax.
# 
#     - Using the SQL query, read the data from the database into a Pandas DataFrame. Review the resulting DataFrame.

# In[39]:


# Wreate a SQL query to join each table in the portfolio into a single DataFrame 
# Use the time column from each table as the basis for the join
query = '''
SELECT GDOT.time, GDOT.daily_returns, GS.daily_returns, PYPL.daily_returns, SQ.daily_returns
FROM GDOT
INNER JOIN GS ON GDOT.time = GS.time
INNER JOIN PYPL ON GDOT.time = PYPL.time
INNER JOIN SQ ON GDOT.time = SQ.time
'''
# 'GDOT', 'GS', 'PYPL', 'SQ'
# SELECT doge.Date, doge.DOGE_Returns, gtc.GTC_Returns
# FROM doge
# JOIN gtc ON gtc.Date = doge.Date

# Using the query, read the data from the database into a Pandas DataFrame
etf_portfolio = pd.read_sql_query(query, con=engine, index_col='time')

# Convert index to datetime
etf_portfolio.index = pd.to_datetime(etf_portfolio.index)

# Create some nicer column names
column_names = [f"{table_name}_daily_returns" for table_name in table_names]
etf_portfolio.columns = column_names

# Review the resulting DataFrame
etf_portfolio


# ### Step 2: Create a DataFrame that averages the “daily_returns” columns for all four assets. Review the resulting DataFrame.

# In[40]:


# Create a DataFrame that displays the mean value of the “daily_returns” columns for all four assets.
etf_portfolio_returns = etf_portfolio.mean(axis=1)

# Review the resulting DataFrame
etf_portfolio_returns


# ### Step 3: Use the average daily returns in the etf_portfolio_returns DataFrame to calculate the annualized returns for the portfolio. Display the annualized return value of the ETF portfolio.

# In[41]:


# Use the average daily returns provided by the etf_portfolio_returns DataFrame 
# to calculate the annualized return for the portfolio.
number_trading_days_in_year = 252 
annualized_etf_portfolio_returns = etf_portfolio_returns * number_trading_days_in_year

# Display the annualized return value of the ETF portfolio.
annualized_etf_portfolio_returns


# ### Step 4: Use the average daily returns in the `etf_portfolio_returns` DataFrame to calculate the cumulative returns of the ETF portfolio.

# In[45]:


# Use the average daily returns provided by the etf_portfolio_returns DataFrame 
# to calculate the cumulative returns
etf_cumulative_returns =  (1 + etf_portfolio_returns).cumprod()

# Display the final cumulative return value
final_cumulative_return_value = etf_cumulative_returns[etf_cumulative_returns.size - 1]

print(f"The cumulative return for an equally weighted portfolio of these ETFs is {final_cumulative_return_value}")


# ### Step 5: Using hvPlot, create an interactive line plot that visualizes the cumulative return values of the ETF portfolio. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.

# In[50]:


# Using hvplot, create an interactive line plot that visualizes the ETF portfolios cumulative return values.
etf_portfolio_cumulative_returns = (1 + etf_portfolio).cumprod()

combined_label = 'Equal Weighted'
etf_portfolio_cumulative_returns[combined_label] = etf_cumulative_returns

display(etf_portfolio_cumulative_returns)

etf_portfolio_cumulative_returns.columns = table_names + [combined_label]

etf_portfolio_cumulative_returns.hvplot.line(
    title="ETF Portfolio Cumulative Returns",
    ylabel="Cumulative Return",
)


# In[ ]:




