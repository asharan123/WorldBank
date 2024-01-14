# ETL-Pyspark-Postgres-Django-Dashboard

## Overview
This project demonstrates an ETL (Extract, Transform, Load) process using PySpark to extract data on Gross Domestic Product (GDP) and Gross National Income (GNI) from the World Bank website through their API. The data is then cleaned, analyzed, and loaded into a PostgreSQL database. Additionally, a Django dashboard app is created to visualize and display the processed data.

## Steps
1. **Data Extraction:** 
   - Extracted GDP and GNI data from the World Bank website using their API by querying relevant datasets.

2. **Data Cleaning:**
   - Utilized PySpark to clean and preprocess the extracted data, handling missing values and inconsistencies.

3. **Data Analysis:**
   - Conducted analysis on the cleaned data, including insights and statistics about different income levels across countries.

4. **Loading into PostgreSQL:**
   - Loaded the processed Spark DataFrame into a PostgreSQL database for further usage and access.

5. **Django Dashboard App:**
   - Created a Django dashboard app to visualize and display the processed data.
   - Integrated the app with the PostgreSQL database to fetch and present real-time insights.

## Project Structure
- `ETL_Pyspark_Postgres.ipynb`: Jupyter Notebook containing the ETL process using PySpark.
- `dashboard/`: Django app directory containing files for the dashboard application.
- `data/`: Directory containing the extracted and cleaned datasets.
- `scripts/`: Additional scripts or SQL files for database operations.

## Usage
1. **Setup:**
   - Ensure the required dependencies are installed: PySpark, PostgreSQL, Django, relevant Python libraries.
   
2. **Data Extraction and ETL:**
   - Run the Jupyter Notebook `ETL_Pyspark_Postgres.ipynb` to execute the ETL process step by step.

3. **Django Dashboard:**
   - Navigate to the `dashboard/` directory.
   - Run the Django development server using `python manage.py runserver`.
   - Access the dashboard app at `http://127.0.0.1:8000/dashboard/` in your web browser.

4. **Accessing the Data:**
   - Processed and cleaned datasets will be available in the `data/` directory.
   - Access the PostgreSQL database through the Django app to query or utilize the loaded data.

## Requirements
- Python 3.10
- PySpark
- PostgreSQL
- Django
- World Bank API access (if data extraction is required)

## References
- [World Bank API Documentation](http://api.worldbank.org/v2/country)
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/index.html)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/current/index.html)
- [Django Documentation](https://docs.djangoproject.com/en/3.2/)
