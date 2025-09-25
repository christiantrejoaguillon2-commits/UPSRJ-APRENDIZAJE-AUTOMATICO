import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog, mlog
# Set logging file for debug
log_file = f"{os.path.basename(__file__).split(sep='.')[0]}.log"
set_logging(log_file=log_file)


class DataSource:
    def __init__(self, url: str):
        self.url = url
        self.data = self.fetch_url()
        self.relevant_features = self.select_relevant_features()
        
    def fetch_url(self):
        data = None
        
        try:
            # TODO: Fetch data from url with pandas and save it into "data"
            # NOTE: https://pandas.pydata.org/docs/dev/reference/api/pandas.read_csv.html
            data = pd.DataFrame()
            mlog(f"Data fetched from source. Review {log_file}", f"Data fetched from source.\n{data.sample(5).to_string()}", level=DEBUG, eol=True)
            
            # TODO: Generate an statistic resume of numeric columns of "data"
            # NOTE: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
            pass
        
        except:
            data = None
            mlog(f"Error fetching source. Review {log_file}", data, level=ERROR, eol=True)
            
        return data

    def select_relevant_features(self):
        relevant_features = None
        
        try:
            # TODO: Create a DataFrame from "data" with some relevant features for our linear regression model.
            #       Consider the real statement. If you are making a linear regression model for estimating
            #       C02 consumption in different vehicles, some relevant features could be:
            #          - The engine size
            #          - The number of cylinders
            #          - The combined fuel consumption
            #          - The CO2 emissions  
            #
            # NOTE: https://www.geeksforgeeks.org/python/different-ways-to-create-pandas-dataframe/#creating-a-dataframe-from-another-dataframe
            relevant_features = pd.DataFrame()
            mlog(f"Data fetched from source. Review {log_file}", f"Data fetched from source.\n{relevant_features.sample(9).to_string()}", level=DEBUG, eol=True)
        except:
            relevant_features = None
            mlog(f"Error fetching source. Review {log_file}", relevant_features, level=ERROR, eol=True)
            
        return relevant_features 
    
    def set_histogram(self, out: str):
        
        try:
            # TODO: Define a method to consider the histograms for each of these features, for this, you'll create a DataFrame "viz" from "relevant_features". 
            #       Plot them and save the image as the "out" value.
            # 
            # NOTE: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.hist.html
            #       https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
            viz = pd.DataFrame()
            plog(f"Created histogram plot {out}", level=INFO, eol=True)
            
        except:
            mlog(f"Error setting histogram. Review {log_file}", viz, level=ERROR, eol=True)
        
    def feature_scatter_plot(x, y, x_label: str, y_label: str, out: str):
        try:
            # TODO: Define a method that displays scatter plots of "relevant_features", to see how linear their relationships are.
            #       The method also needs to save the image as the "out" value.
            #
            # NOTE: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html
            #       https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
            plog(f"Created scatter plot {out}", level=INFO, eol=True)

        except:
            plog(f'Error creating scatter plot for "{x_label}" & "{y_label}".', level=ERROR, eol=True)
            
    def extract_data(self, feature):
        data = None
        
        try:
            # TODO: Define a method that extracts the data from features of "relevant_features" as numpy type, assign the value to "data".
            # 
            # NOTE: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html
            data = np.zeros(0)
            mlog(f"{feature} data extracted from source. Review {log_file}", data, level=DEBUG, eol=True)
        
        except:
            plog(f'Error extracting {feature} data.', level=ERROR, eol=True)
            
        return data