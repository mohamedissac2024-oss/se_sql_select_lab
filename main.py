# STEP 1A
# Import SQL Library and Pandas

import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')


# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""SELECT employeeNumber, lastName FROM employees""", conn)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber FROM employees""", conn)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""SELECT employeeNumber as ID, lastName FROM employees""", conn)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql("""
SELECT 
    CASE 
        WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') THEN 'Executive'
        ELSE 'Not Executive'
    END AS role,
    employeeNumber, lastName, jobTitle
FROM employees
""", conn)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""SELECT LENGTH(lastName) AS name_length FROM employees""", conn)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""SELECT SUBSTR(jobTitle, 1, 2) AS short_title FROM employees""", conn)


# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""SELECT SUM(ROUND(priceEach * quantityOrdered)) as total FROM orderDetails""", conn)['total']

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""
SELECT
    orderDate,
    strftime('%d', orderDate) AS day,
    strftime('%m', orderDate) AS month,
    strftime('%Y', orderDate) AS year
FROM orders
""", conn)


# ---------------------------------------------------------------
# Running `python3 main.py` inspects the results of each step.
# ---------------------------------------------------------------
if __name__ == "__main__":
    # Reference queries provided in the README
    employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
    order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)

    results = {
        "Employee Data": employee_data,
        "Order Details Data": order_details,
        "STEP 2 df_first_five": df_first_five,
        "STEP 3 df_five_reverse": df_five_reverse,
        "STEP 4 df_alias": df_alias,
        "STEP 5 df_executive": df_executive,
        "STEP 6 df_name_length": df_name_length,
        "STEP 7 df_short_title": df_short_title,
        "STEP 8 sum_total_price": sum_total_price,
        "STEP 9 df_day_month_year": df_day_month_year,
    }

    for title, result in results.items():
        print(f"---------------------{title}---------------------")
        print(result)
        print(f"-------------------End {title}-------------------")

    # Close the connection to the database
    conn.close()
