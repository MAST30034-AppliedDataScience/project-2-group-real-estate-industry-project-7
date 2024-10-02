# Generic Real Estate Consulting Project

This project aims to predict rental prices for residential properties and apartments throughout Victoria, Australia, using both internal and external variables. The goal is to help an online real estate company determine appropriate rental prices and identify properties with the potential for rental price growth over the next five years.

## Introduction

The real estate industry is highly dynamic, with rental prices influenced by a wide range of internal and external factors. This project explores how attributes such as property features (e.g., number of bedrooms, car spaces, land size) and geospatial attributes (e.g., proximity to schools, train stations, parks) impact rental prices in Victoria, Australia. The primary objective is to build predictive models that can estimate rental prices and provide insights on potential price increases in the near future.

## Project Overview

1. Scrape rental property data and internal attributes (e.g., number of bedrooms, land size, car park spots) from domain.com.au use API.
2. Incorporate external variables such as population demographics (e.g., population growth and affluence in SA2 districts), use Statistical Areas Level 2 (SA2) to derive population forecast and affluence
3. Use openrouteservice API to find proximity to train stations, closest schools and CBD.
4. Identify the most important internal and external features in predicting rental prices.
5. Identify the most liveable and affordable suburbs
6. Use machine learning models to predict rental prices and find top 10 suburbs with the highest predicted growth rate.

## Running the Project

To successfully run the project, follow these steps in order:

1. **Data Collection**

   - Start by running the `rental_properties_download.ipynb` and `external_data_download.ipynb` notebooks to scrape property and demographic data from the specified websites. This will generate the necessary datasets for analysis. _(Note: Collecting data from Domain may take a considerable amount of time; alternatively, you can use the data directly from `rent_info.json`.)_

2. **Data Preprocessing**

   - Next, execute the `external_data_process.ipynb` and `internal_data_process.ipynb` notebooks to clean and prepare the data for modeling. This ensures that all datasets are properly formatted and that any missing values are addressed.
   - Then, run the `openrouteservice_school.ipynb` and `distance_to_CBD_train.ipynb` notebooks to calculate proximity to train stations, the closest schools, and the CBD. _(Note: This step may also require significant time from ORS; alternatively, you can use the data directly from **TO BE UPDATED**.csv.)_
   - To visualize the geospatial distribution of the scraped rental properties, you can run `geolocation_properties.ipynb`.
   - To utilize Statistical Areas Level 2 (SA2) for deriving population forecasts and affluence metrics, run `affluence.ipynb` and `population_forecast.ipynb`.
   - Finally, to ensure we can match the internal and external datasets for future analysis, run `add_postcode.ipynb` to add postcodes to the corresponding datasets.

3. **Data Analysis**

   - After preprocessing, run **TO BE UPDATED** to visualize the relationships between rental prices and other internal and external features. This will help you gain deeper insights into the data.

4. **Modeling**

   - **TO BE UPDATED**

5. **Others**
   - To identify the most livable and affordable suburbs, execute the `livable.ipynb` and `affordable.ipynb` notebooks.
