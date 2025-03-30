OUR FINAL PROJECT :-  Attached Folder - Final_Project
Note: app.py (backend) to be running before index.html is launched. 

FRONTEND PROTOTYPE :- https://singular-beijinho-42fe07.netlify.app

# Hacknite
CODEBYTE'S PROJECT FOR HACKNITE
🌍 Project Overview

This project aims to develop an integrated AI system leveraging remote sensing data, climate modelling, and urban analytics to optimize renewable energy generation and urban green space development. Our solution focuses on biodiversity conservation and environmental sustainability while harmonizing energy grids, ecological habitats, and urban infrastructure.

# Problem Statement Analysis

Urban environments face increasing challenges due to climate variability, pollution, and energy demands. Our goal is to use AI to provide actionable insights for resource management and urban planning, addressing the following:
1. Where and which renewable resources can be installed for optimal efficiency.
2. How to enhance green cover in specific regions to combat pollution.
3. Ways to improve biodiversity conservation and environmental sustainability.

# Libraries Used 

1. Pandas
2. NumPy
3. Matplotlib
4. Seaborn
5. Flask → Web framework to create API
6. scikit-learn → Machine learning library for Random Forest
7. joblib → Save and load trained ML models


# Project Workflow

1. Data Collection & Processing:
   We used datasets from Kaggle, focusing on three primary sources:


     I. Raw data
        
         a) Rainfall in India 1901-2015.csv
      
            Used for historical analysis and AI-driven prediction for 2016-2025.
            Cities selected: Delhi, Chennai, and Bengaluru (due to data availability).
            Kolkata and Mumbai were excluded due to insufficient data overlap.

         b) city_day.csv (2015-2020) 

           Derived monthly average pollution levels (AQI) for Delhi, Chennai, and Bengaluru.
           AI-based prediction generated values for 2021-2025.

         c) Sunshine hours for cities in the world.csv 

           Provided monthly average sunshine hours for global cities (1961-1990)
           AI-driven sunshine forecasts for 2015-2025.
  
     II. Made three separate csv files - a)Rainfall_updated(2015-2025).csv, b)Monthly_Sunshine_Forecast_2015_2025.csv, c)AQI(dcb).csv and merged them to                        obtain "FINAL_DATASET.csv" using pandas.

#
2. The frontend prototype was heavily based on data and was created using bolt.new. However it did not use a ML model.

#
3. Final_Project
   
      I. Solar Potential Prediction - Random Forest Regression

     II. Wind Energy Assessment - Gradient Boosting Regressor (XGBoost)
  
     III. Air Quality Index - U-Net (Semantic Segmentation)

     IV. Green Cover Analysis - LSTM Neural Network

     V. Recommendation Engine - Ensemble Classifier (Random Forest + SVM)

#
4. Outcome
   
      I. Annual sunshine hours, peak sun hours, and solar viability score
   
      II. Wind potential rating (1-5 scale) and optimal turbine placement suggestions
   
      III. Percentage of green cover, Tree canopy density map, Biodiversity hotspot identification
   
      IV. AQI prediction and pollution source attribution
   
      V. Customized renewable energy recommendations with feasibility scores

      VI. Website-based AI insights for urban planners and policymakers.

#
5. Requirements

      pip install pandas, numpy, flask, scikit-learn, joblib, requests, matplotlib, seaborn, plotly
   

   
   

