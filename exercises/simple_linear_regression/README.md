# **Simple Linear Regression**

**Instructor:** Jesus Salvador Lopez Ortega ([LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport))

---
## **Index**
- [**Simple Linear Regression**](#simple-linear-regression)
  - [**Index**](#index)
  - [**Due Date**](#due-date)
- [**CO2 Emissions Data Analysis**](#co2-emissions-data-analysis)
  - [📘 Overview](#-overview)
  - [🎯 Objectives](#-objectives)
  - [📂 Files](#-files)
  - [🛠️ Instructions](#️-instructions)
    - [1. `fetch_url()`](#1-fetch_url)
    - [2. `select_relevant_features()`](#2-select_relevant_features)
    - [3. `set_histogram(out)`](#3-set_histogramout)
    - [4. `feature_scatter_plot(x, y, x_label, y_label, out)`](#4-feature_scatter_plotx-y-x_label-y_label-out)
    - [5. `extract_data(feature)`](#5-extract_datafeature)
- [**Simple Linear Regression: Part 1**](#simple-linear-regression-part-1)
  - [📘 Overview](#-overview-1)
  - [🎯 Objectives](#-objectives-1)
  - [📂 File](#-file)
  - [🛠️ Instructions](#️-instructions-1)
    - [1. Exercise 1 – Histogram](#1-exercise-1--histogram)
    - [2. Exercise 2 – Combined Fuel Consumption vs CO₂ Emission](#2-exercise-2--combined-fuel-consumption-vs-co-emission)
    - [3. Exercise 3 – Number of Cylinders vs CO₂ Emission](#3-exercise-3--number-of-cylinders-vs-co-emission)
- [**Simple Linear Regression: Part 2**](#simple-linear-regression-part-2)
  - [📘 Overview](#-overview-2)
  - [🎯 Objectives](#-objectives-2)
  - [📂 File](#-file-1)
  - [🛠️ Instructions](#️-instructions-2)
    - [Step 1 – Extract Features](#step-1--extract-features)
    - [Step 2 – Split Data](#step-2--split-data)
    - [Step 3 – Create Model](#step-3--create-model)
    - [Step 4 – Train Model](#step-4--train-model)
    - [Step 5 – Extract Coefficients](#step-5--extract-coefficients)
    - [Step 5.1 – Visualize Training Fit](#step-51--visualize-training-fit)
    - [Step 6 – Predict and Evaluate](#step-6--predict-and-evaluate)
    - [Step 7 – Visualize Test Fit](#step-7--visualize-test-fit)
- [**Homework: Fuel Consumption Regression**](#homework-fuel-consumption-regression)
  - [📘 Overview](#-overview-3)
  - [🎯 Objective](#-objective)
  - [🛠️ Instructions](#️-instructions-3)
- [**Understand the data**](#understand-the-data)
    - [`FuelConsumption.csv`:](#fuelconsumptioncsv)
  - [**Contact**](#contact)

---

## **Due Date**
- **Start Date:** September 25, 2025
- <span style="color:gold"><b>Due date:</b> October 2, 2025 ⏰</span>

---

# **CO2 Emissions Data Analysis**

## 📘 Overview

This project introduces students to exploratory data analysis and feature selection using a real-world dataset related to vehicle fuel consumption and CO₂ emissions. The goal is to prepare the data for a linear regression model by identifying relevant features and visualizing their relationships.

## 🎯 Objectives

Students will:

- Load and inspect a dataset from a remote source
- Select meaningful features for regression modeling
- Generate histograms and scatter plots for visual analysis
- Extract feature data as NumPy arrays
- Practice logging and debugging in a reproducible pipeline

## 📂 Files

- `data_source.py`: Main class for data loading, feature selection, and visualization
- `simple_linear_regression.py`: 
  
## 🛠️ Instructions

Each method in `data_source.py` contains `TODO` comments. Your task is to **complete each TODO** using the documentation links provided. Specifically:

### 1. `fetch_url()`

- Load the dataset using `pandas.read_csv()`
- Generate a statistical summary using `.describe()`

### 2. `select_relevant_features()`

- Create a new DataFrame with features relevant to CO₂ prediction
- Suggested features:
  - Engine size
  - Number of cylinders
  - Combined fuel consumption
  - CO₂ emissions

### 3. `set_histogram(out)`

- Plot histograms for each selected feature using `.hist()`
- Save the plot to the specified output path using `plt.savefig(out)`

### 4. `feature_scatter_plot(x, y, x_label, y_label, out)`

- Create a scatter plot between two features
- Save the plot to the specified output path

### 5. `extract_data(feature)`

- Extract a single feature column as a NumPy array using `.to_numpy()`

---

# **Simple Linear Regression: Part 1**

## 📘 Overview

This exercise guides students through the first steps of building a simple linear regression model using selected features from a dataset on vehicle fuel consumption and CO₂ emissions. The focus is on visualizing relationships between variables and understanding their linearity.

## 🎯 Objectives

Students will:

- Generate histograms to explore feature distributions
- Create scatter plots to assess linear relationships
- Prepare visual outputs for regression modeling
- Practice reproducible plotting and file management

## 📂 File

- `simple_linear_regression.py`: Contains three exercises with `TODO` sections to complete

## 🛠️ Instructions

The file is divided into three exercises. Your task is to **complete each TODO** using the specified output paths and plotting methods.

### 1. Exercise 1 – Histogram

- Generate histograms for all relevant features using the `DataSource` class

### 2. Exercise 2 – Combined Fuel Consumption vs CO₂ Emission

- Create a scatter plot comparing the `Combined Fuel Consumption` feature against `CO2 Emission`

### 3. Exercise 3 – Number of Cylinders vs CO₂ Emission

- Create a scatter plot comparing the `Number of Cylinders` feature against `CO2 Emission`

---

# **Simple Linear Regression: Part 2**

## 📘 Overview

In this second part of the exercise, students will build and evaluate a simple linear regression model to predict CO₂ emissions based on engine size. The goal is to walk through the full modeling pipeline—from data extraction to training, evaluation, and visualization.

## 🎯 Objectives

Students will:

- Extract input and target variables from a prepared dataset
- Split data into training and testing sets
- Create and train a linear regression model
- Visualize the fitted line over training and test data
- Evaluate model performance using standard regression metrics

## 📂 File

- `simple_linear_regression.py`: Contains three exercises with `TODO` sections to complete

## 🛠️ Instructions

The file is divided into three exercises. Your task is to **complete each TODO** using the specified output paths and plotting methods.

### Step 1 – Extract Features

- Use the `DataSource` object to extract:
  - `X`: Engine Size (input feature)
  - `y`: CO₂ Emissions (target output)
- Convert both to NumPy arrays using `.to_numpy()`

### Step 2 – Split Data

- Use `train_test_split()` from `sklearn.model_selection`
- Split the data into 80% training and 20% testing
- Set `random_state=42` for reproducibility

### Step 3 – Create Model

- Instantiate a `LinearRegression` object from `sklearn.linear_model`

### Step 4 – Train Model

- Reshape `X_train` to a 2D array: `(n_samples, 1)`
- Fit the model using `regressor.fit(X_train, y_train)`

### Step 5 – Extract Coefficients

- Retrieve:
  - `regressor.coef_`
  - `regressor.intercept_`
- Log the values for debugging

### Step 5.1 – Visualize Training Fit

- Plot the training data and the fitted regression line

### Step 6 – Predict and Evaluate

- Use `regressor.predict(X_test)` to generate predictions
- Evaluate the model using:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Step 7 – Visualize Test Fit

- Plot the test data and the predicted regression line

---

# **Homework: Fuel Consumption Regression**

## 📘 Overview

In this final task, students will apply the same linear regression modeling process as before, but using a different input feature: **Fuel Consumption**. The goal is to compare the performance of this model against the previous one based on **Engine Size**, using identical data splits and evaluation metrics.

## 🎯 Objective

Build a new linear regression model using **Fuel Consumption** as the input feature and **CO₂ Emissions** as the target. Evaluate its performance and assign the label of the best-performing model to the variable `best_model`.

## 🛠️ Instructions

Complete the final `TODO` in the file by following these steps:

1. **Extract Feature and Target**
   - Use the `DataSource` object to extract:
     - `X`: Fuel Consumption (input feature)
     - `y`: CO₂ Emissions (target output)
   - Convert both to NumPy arrays

2. **Split Data**
   - Use `train_test_split()` with:
     - 80% training, 20% testing
     - `random_state=42` (same as before)

3. **Create and Train Model**
   - Instantiate and train a `LinearRegression` model
   - Reshape `X_train` to 2D if needed

4. **Evaluate Model**
   - Use the same metrics:
     - Mean Absolute Error (MAE)
     - Mean Squared Error (MSE)
     - Root Mean Squared Error (RMSE)
     - R² Score

5. **Assign Best Model**
   - Based on your evaluation, assign the label of the best-performing input feature to:
     ```python
     best_model = "<COLUMN_LABEL>"

---

# **Understand the data**

### `FuelConsumption.csv`:
You will use a fuel consumption dataset, **`FuelConsumption.csv`**, which contains model-specific fuel consumption ratings and estimated carbon dioxide emissions for new light-duty vehicles for retail sale in Canada. [Dataset source](http://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64).

- **MODEL YEAR** e.g. 2014
- **MAKE** e.g. VOLVO
- **MODEL** e.g. S60 AWD
- **VEHICLE CLASS** e.g. COMPACT
- **ENGINE SIZE** e.g. 3.0
- **CYLINDERS** e.g 6
- **TRANSMISSION** e.g. AS6
- **FUEL TYPE** e.g. Z
- **FUEL CONSUMPTION in CITY(L/100 km)** e.g. 13.2
- **FUEL CONSUMPTION in HWY (L/100 km)** e.g. 9.5
- **FUEL CONSUMPTION COMBINED (L/100 km)** e.g. 11.5
- **FUEL CONSUMPTION COMBINED MPG (MPG)** e.g. 25
- **CO2 EMISSIONS (g/km)** e.g. 182 

Your task will be to create a simple linear regression model from one of these features to predict CO2 emissions of unobserved cars based on that feature. 

## **Contact**

¿Any doubt? Check the support files or contact your instructor.

**Politécnica de Santa Rosa**

- **Carreer: ISW**
- **Assignature: Software Architectures**
- **Author:** Jesus Salvador Lopez Ortega ([LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport))
- **Last updated**: September 2025