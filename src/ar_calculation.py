import os
import pandas as pd

# Data root: original absolute paths replaced with a configurable root.
# Point EVENT_STUDY_DATA at the folder holding OLS/, UK Result/,
# Event_Analysis_Output/, etc. Defaults to <repo>/data.
DATA_ROOT = os.environ.get(
    "EVENT_STUDY_DATA",
    os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")))


# Define the folder containing the expected return files
expected_return_folder = DATA_ROOT + "/Event_Analysis_Output/Expected_Returns"
ar_output_folder = DATA_ROOT + "/Event_Analysis_Output/Abnormal_Returns"

# Ensure the output folder for AR files exists
if not os.path.exists(ar_output_folder):
    os.makedirs(ar_output_folder)

# Function to calculate AR and save results
def calculate_abnormal_return(file_path, output_folder):
    try:
        # Load the expected return file
        df = pd.read_csv(file_path)
        
        # Ensure the necessary columns are present
        if 'Industry_Return' in df.columns and 'Expected_Return' in df.columns:
            # Calculate Abnormal Return (AR)
            df['Abnormal_Return'] = df['Industry_Return'] - df['Expected_Return']
            
            # Save the updated dataframe to a new file
            file_name = os.path.basename(file_path).replace("_Expected_Returns.csv", "_Abnormal_Returns.csv")
            output_path = os.path.join(output_folder, file_name)
            df.to_csv(output_path, index=False)
            print(f"Abnormal returns saved to: {output_path}")
        else:
            print(f"'Industry_Return' or 'Expected_Return' column missing in file: {file_path}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Process each file in the expected return folder
for file_name in os.listdir(expected_return_folder):
    if file_name.endswith("_Expected_Returns.csv"):
        file_path = os.path.join(expected_return_folder, file_name)
        calculate_abnormal_return(file_path, ar_output_folder)
