import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import exercises.simple_linear_regression.data_source as ds
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog, mlog
# Set logging file for debug
log_file = f"{os.path.basename(__file__).split(sep='.')[0]}.log"
set_logging(log_file=log_file)    
       
FUEL_CONSUMPTION_CO2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"

#########################################################################################################################
# For the first part, you will analyze the linear relationship between the relevant features                            #
#########################################################################################################################

# Exercise 1
# TODO: Create the histogram from the data source.
#       The name of the output plot must be "./exercises/simple_linear_regression/outputs/histogram.png"
pass

# Exercise 2
# TODO: Plot the Combined Fuel Consumption feature against CO2 Emission, to see how linear their relationship is.
#       The name of the output plot must be "./exercises/simple_linear_regression/outputs/<x_label>_vs_<y_label>.png"
pass

# Exercise 3
# TODO: Plot the Number of Cylinders feature against CO2 Emission, to see how linear their relationship is.
#       The name of the output plot must be "./exercises/simple_linear_regression/outputs/<x_label>_vs_<y_label>.png"
pass

#########################################################################################################################
# For the second part, you will use Engine Size to predict CO2 Emissions with a linear regression model.                #
# Follow the steps bellow                                                                                               #
#########################################################################################################################

# Step 1 
# TODO: Extract the input feature and target output variables, X and y, from the DataSource object. The data should be numpy type.
# 
# NOTE: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html

X = None
plog(f'Variable "X" not defined' if X is None else f'Defined variable "X". Review {log_file}', level=ERROR if X is None else DEBUG, eol=True)

y = None
plog(f'Variable "y" not defined' if y is None else f'Defined variable "y". Review {log_file}', level=ERROR if y is None else DEBUG, eol=True)

# Step 2
# TODO: Split data for training & testing, using 80% of the dataset for training and reserving the remaining 20% for testing.
#       Random state should be 42 for this case.
#
# NOTE: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

X_train, X_test, y_train, y_test = None, None, None, None

mlog(f'Data not splitted.' if any([X_train is None, y_train is None, X_test is None, y_test is None]) else f'Defined data for training. Review {log_file}', f'Defined data for training:\nX:\n{X_train}\nY:\n{y_train}', 
     level=ERROR if any([X_train is None, y_train is None, X_test is None, y_test is None]) else DEBUG, eol=True)

# Step 3:
# TODO: Create a model object.
#
# NOTE: https://scikit-learn.org/stable/modules/linear_model.html
plog(f'Creating model...')
regressor = None
plog('Regressor not created' if regressor is None else f'done.', level=ERROR if regressor is None else INFO, eol=True)

# Step 4:
# TODO: Train the model on the training data.
#       Notice that "X_train" is a 1-D array but sklearn models expect a 2D array as input for the training data, 
#       with shape (n_observations, n_features).
#
# NOTE: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html
#       https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.fit
plog(f'Training model with data...')
pass
plog('Regressor not created' if regressor is None else f'done.', level=ERROR if regressor is None else INFO, eol=True)

# Step 5:
# TODO: Obtain the regressor coefficients & intercept.
#
# NOTE: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression
coefficients = None
mlog(f'Coefficients not obtained.' if coefficients is None else f'Coefficients obtained. Review {log_file}', f'Regressor coefficients obtained:\n{coefficients}', level=ERROR if coefficients is None else DEBUG, eol=True)

intercept = None
mlog(f'Intercept not obtained' if intercept is None else f'Intercept obtained. Review {log_file}', f'Regressor intercept obtained:\n{intercept}', level=ERROR if intercept is None else DEBUG, eol=True)

# Step 5.1: 
# TODO: visualize the goodness-of-fit of the model to the training data by plotting the fitted line over the data.
#       The regression model is the line given by y = intercept + coefficient * x.
#       Save the image as "./exercises/simple_linear_regression/outputs/train_engine_size.png"
#
# NOTE: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
plog(f"Creating linear regression model plot...")
pass
plog(f'Regressor Training plot not created.' if not os.path.exists("./exercises/simple_linear_regression/outputs/train_engine_size.png") else f'done.', 
     level=ERROR if not os.path.exists("./exercises/simple_linear_regression/outputs/train_engine_size.png") else DEBUG, eol=True)

# Step 6:
# TODO: Use the predict method to make test predictions. Assign value to "y_test_"
#
# NOTE: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.predict
y_test_ = None

# Model evaluation
# 
# You can compare the actual values and predicted values to calculate the accuracy of a regression model. Evaluation metrics play a key role in the development of a model, 
# as they provide insight into areas that require improvement.
# There are different model evaluation metrics, let's use MSE here to calculate the accuracy of our model based on the test set:
#   - Mean Absolute Error: It is the mean of the absolute value of the errors. This is the easiest of the metrics to understand since it’s just an average error.
#   - Mean Squared Error (MSE): MSE is the mean of the squared error. In fact, it's the metric used by the model to find the best fit line, and for that reason, it is also called the residual sum of squares.
#   - Root Mean Squared Error (RMSE). RMSE simply transforms the MSE into the same units as the variables being compared, which can make it easier to interpret.
#   - R-squared is not an error but rather a popular metric used to estimate the performance of your regression model. It represents how close the data points are to the fitted regression line. 
#     The higher the R-squared value, the better the model fits your data. The best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse).

# Evaluation
try:
    plog("Mean absolute error: %.2f" % mean_absolute_error(y_test, y_test_), level=DEBUG)
    plog("Mean squared error: %.2f" % mean_squared_error(y_test, y_test_),  level=DEBUG)
    plog("Root mean squared error: %.2f" % np.sqrt(mean_squared_error(y_test, y_test_)),  level=DEBUG)
    plog("R2-score: %.2f" % r2_score(y_test, y_test_), level=DEBUG, eol=True)
except:
    plog("Error evaluating the model, please check your data & process.", level=ERROR, eol=True)
    
# Step 7:
# TODO: Plot the regression model result over the test data instead of the training data. 
#       Visually evaluate whether the result is good and save the image as "./exercises/simple_linear_regression/outputs/test_engine_size.png"
#
# NOTE: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
plog(f"Creating linear regression model evalation plot...")
pass

plog(f'Regressor Evaluation plot not created.' if not os.path.exists("./exercises/simple_linear_regression/outputs/test_engine_size.png") else f'done.', 
     level=ERROR if not os.path.exists("./exercises/simple_linear_regression/outputs/test_engine_size.png") else DEBUG, eol=True)

#########################################################################################################################
# ** HOMEWORK **                                                                                                        #
# TODO: Perform a linear regression model as the previos, selecting the Fuel Consumption feature now.                   #
#       Assign the best-fit model dataframe column label to "best_model".                                               # 
#                                                                                                                       #
# NOTE: Use the same random state & data split percentage as previously so you can make an objective comparison to the  # 
#       previous training result.                                                                                       #
#########################################################################################################################
best_model = None

plog(f"Best model: {best_model}", level=ERROR if best_model is None else DEBUG, eol=True)