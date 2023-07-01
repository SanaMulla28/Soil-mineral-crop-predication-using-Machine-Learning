#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Python Packages included
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

import pdb

# File Paths
INPUT_PATH = "../inputs/DATASET2.csv"
OUTPUT_PATH = "../inputs/test.csv"

# Headers
HEADERS = ["Nitrogen", "Phosphorous", "potassium", "organiccarbon", "pH"]


def read_data(path):
    """
    Read the data into pandas dataframe
    :param path:
    :return:
    """
    data = pd.read_csv(path)
    return data


def get_headers(dataset,test):
    """
    dataset headers
    :param dataset:
    :return:
    """
    return dataset.columns.values,test.columns.values


def add_headers(dataset, headers):
    """
    Add the headers to the dataset
    :param dataset:
    :param headers:
    :return:
    """
    dataset.columns = headers
    return dataset


def data_file_to_csv():
    """

    :return:
    """

    # Headers
    headers = ["Nitrogen", "Phosphorous", "potassium", "organiccarbon","pH"]
    # Load the dataset into Pandas data frame
    dataset = read_data(INPUT_PATH)
    # Add the headers to the loaded dataset
    dataset = add_headers(dataset, headers)
    # Save the loaded dataset into csv format
    dataset.to_csv(OUTPUT_PATH, index=False)
    #print "File saved ...!"


def split_dataset(dataset, train_percentage, feature_headers, target_header):
    """
    Split the dataset with train_percentage
    :param dataset:
    :param train_percentage:
    :param feature_headers:
    :param target_header:
    :return: train_x, test_x, train_y, test_y
    """

    # Split dataset into train and test dataset
    train_x, test_x, train_y, test_y = train_test_split(dataset[feature_headers], dataset[target_header],
                                                        train_size=train_percentage)
    return train_x, test_x, train_y, test_y


def handel_missing_values(dataset, missing_values_header, missing_label):
    """
    Filter missing values from the dataset
    :param dataset:
    :param missing_values_header:
    :param missing_label:
    :return:
    """

    #return dataset[dataset[missing_values_header] != missing_label]


def random_forest_classifier(features, target):
    """
    To train the random forest classifier with features and target data
    :param features:
    :param target:
    :return: trained random forest classifier
    """
    clf = RandomForestClassifier()
    clf.fit(features, target)
    return clf


def main():
    """
    Main function
    :return:
    """
    # Load the csv file into pandas dataframe
    dataset = pd.read_csv(INPUT_PATH)
    test= pd.read_csv(OUTPUT_PATH)
  


    train_x, test_x, train_y, test_y = split_dataset(dataset, 0.7, HEADERS[1:-1], HEADERS[-1])

  
    # Create random forest classifier instance
    trained_model = random_forest_classifier(train_x, train_y)
    
    
    predictions = trained_model.predict(test)

    
    print ("Predicted pH ::", predictions)

   
    if predictions in range(5,6):
        rs="predicted crop is Maize" 
    elif predictions in range(6,7):
        rs=("predicted crop is Wheat & Maize")
    elif predictions in range(7,8):
        rs=("predicted crop is Jowar & Sunflower")
    elif predictions in range(8,9):
        rs=("Soil pH is not suitable for any crop in this region")
    out="Predicted pH ::"+str(predictions)+"\n"+rs
    print(out)
    return out
    

if __name__ == "__main__":
    main()
    


# In[ ]:





# In[ ]:




