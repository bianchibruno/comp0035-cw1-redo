# ChatGPT-4: Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# ChatGPT-4: Function to load the dataset
def load_dataset(filepath):
    """
    Load the dataset from a given CSV file.
    
    Parameters:
    - filepath (str): The path to the CSV file.
    
    Returns:
    - pandas.DataFrame: Loaded data.
    """
    # ChatGPT-4: Attempt to read the CSV file and return the DataFrame
    try:
        data = pd.read_csv(filepath)
        print("Dataset loaded successfully.")
        return data
    except Exception as e:
        print(f"Failed to load dataset: {e}")

# ChatGPT-4: Function to save the dataset
def save_dataset(data, filepath):
    """
    Save the dataset to a CSV file.
    
    Parameters:
    - data (pandas.DataFrame): The DataFrame to save.
    - filepath (str): The path to the CSV file where the data will be saved.
    """
    # ChatGPT-4: Attempt to save the DataFrame to a CSV file
    try:
        data.to_csv(filepath, index=False)
        print("Dataset saved successfully.")
    except Exception as e:
        print(f"Failed to save dataset: {e}")

def clean_data(data):
    """
    Clean and prepare the data for the dashboard.

    Parameters:
    - data (pandas.DataFrame): The loaded data.

    Returns:
    - pandas.DataFrame: Cleaned data ready for visualization.
    """
    # ChatGPT-4: Keep only the necessary columns
    # Programmer: Columns reordered in order to keep original order
    columns_to_keep = ['Case Type',
                       'Status',
                       'Request Received (Year)',
                       'Request Received (Quarter)',
                       'Request Received (Month)',
                       'Case Active Days (grouped)'

    ]
    data = data[columns_to_keep]

   # ChatGPT-4: Fill missing values in specified columns with 'Unknown'
    for column in columns_to_keep:
        data[column].fillna('Unknown', inplace=True)

    return data

def print_unique_values(data):
    """
    Prints unique values for each column in the DataFrame.

    Parameters:
    - data (pandas.DataFrame): The DataFrame to analyze.
    """
    for column in data.columns:
        print(f"Unique values in '{column}':")
        print(data[column].unique())
        print("\n")  # Adds a newline for better readability between columns

# ChatGPT-4: Main block to execute the functions
def main():
    # ChatGPT-4: Load the dataset from 'dataset.csv' in the current directory
    dataset_path = 'dataset.csv'
    cleaned_dataset_path = 'dataset_prepared.csv'

    data = load_dataset(dataset_path)

    if data is not None:
        # ChatGPT-4: Clean the data
        data_cleaned = clean_data(data)

        # ChatGPT-4: Save the cleaned data
        save_dataset(data_cleaned, cleaned_dataset_path)

        print_unique_values(data_cleaned)
    # print(data_cleaned.shape)
    # print(data_cleaned.head(7))
    # print(data_cleaned.info())
    # print(data_cleaned.describe())


if __name__ == "__main__":
    main()

