# ETL-Pyspark-Postgres

## Overview
This project demonstrates an ETL (Extract, Transform, Load) process using PySpark to extract data on Gross Domestic Product (GDP) and Gross National Income (GNI) from the World Bank website through their API. The data is then cleaned, analyzed, and finally loaded into a PostgreSQL database.

## Steps
1. **Data Extraction:** 
   - Extracted GDP and GNI data from the World Bank website using their API by querying relevant datasets.

2. **Data Cleaning:**
   - Utilized PySpark to clean and preprocess the extracted data, handling missing values and inconsistencies.

3. **Data Analysis:**
   - Conducted analysis on the cleaned data, including insights and statistics about different income levels across countries.

4. **Loading into PostgreSQL:**
   - Loaded the processed Spark DataFrame into a PostgreSQL database for further usage and access.

## Project Structure
- `ETL_Pyspark_Postgres.ipynb`: Jupyter Notebook containing the ETL process using PySpark.
- `data/`: Directory containing the extracted and cleaned datasets.
- `scripts/`: Additional scripts or SQL files for database operations.

## Usage
1. **Setup:**
   - Ensure the required dependencies are installed: PySpark, PostgreSQL, relevant Python libraries.
   
2. **Data Extraction and ETL:**
   - Run the Jupyter Notebook `ETL_Pyspark_Postgres.ipynb` to execute the ETL process step by step.

3. **Accessing the Data:**
   - Processed and cleaned datasets will be available in the `data/` directory.
   - Access the PostgreSQL database to query or utilize the loaded data.

## Requirements
- Python 3.x
- PySpark
- PostgreSQL
- World Bank API access (if data extraction is required)

## References
- [World Bank API Documentation](http://api.worldbank.org/v2/country)
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/index.html)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/current/index.html)
