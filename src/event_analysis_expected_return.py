import os
import pandas as pd
import numpy as np
import re

# Define folders for OLS data and return files
ols_folders = [
    r"C:\Users\marco\OneDrive\Escritorio\OLS\Transportation and Infrastructure",
    r"C:\Users\marco\OneDrive\Escritorio\OLS\Agriculture and Food",
    r"C:\Users\marco\OneDrive\Escritorio\OLS\Automotive",
    r"C:\Users\marco\OneDrive\Escritorio\OLS\Defense and Aerospace",
    r"C:\Users\marco\OneDrive\Escritorio\OLS\Energy and Utilities",
    r"C:\Users\marco\OneDrive\Escritorio\OLS\Finance and Insurance",
    r"C:\Users\marco\OneDrive\Escritorio\OLS\Healthcare and Pharmaceuticals",
    r"C:\Users\marco\OneDrive\Escritorio\OLS\Manufacturing and Industrial Goods",
    r"C:\Users\marco\OneDrive\Escritorio\OLS\Real Estate and Construction",
    r"C:\Users\marco\OneDrive\Escritorio\OLS\Retail and Consumer Goods",
    r"C:\Users\marco\OneDrive\Escritorio\OLS\Technology and Telecommunications"
]

returns_folder = r"C:\Users\marco\OneDrive\Escritorio"  # Folder with 30-day returns for each industry

# Function to extract alpha and beta from the OLS file name
def extract_alpha_beta(filename):
    match = re.search(r"([A-Za-z_]+)_([A-Za-z_]+)_([A-Za-z_]+)_OLS.csv", filename)
    if match:
        alpha = float(match.group(2))  # Assuming alpha is in the second position
        beta = float(match.group(3))   # Assuming beta is in the third position
        return alpha, beta
    return None, None

# Loop through each folder and process OLS and return data
for ols_folder in ols_folders:
    print(f"Processing folder: {ols_folder}")
    ols_files = [f for f in os.listdir(ols_folder) if f.endswith('_OLS.csv')]  # Get all OLS files
    
    # Loop through the OLS files to extract alpha and beta values
    for ols_file in ols_files:
        # Get the industry and event name from the OLS file (without the "_OLS.csv" part)
        industry_event = ols_file.replace('_OLS.csv', '')
        print(f"Processing OLS file: {ols_file} for event: {industry_event}")
        
        # Extract alpha and beta values
        alpha, beta = extract_alpha_beta(ols_file)
        
        if alpha is None or beta is None:
            print(f"Skipping {ols_file}, could not extract alpha and beta")
            continue
        
        # Match the corresponding return file
        return_file = f"{industry_event}.csv"
        return_file_path = os.path.join(returns_folder, return_file)
        
        if os.path.exists(return_file_path):
            print(f"Processing return file: {return_file}")
            return_data = pd.read_csv(return_file_path)
            
            # Calculate the expected return using the formula
            return_data['Expected_Return'] = alpha + beta * return_data['Market_Return']
            
            # Save the output to a new file
            output_file = os.path.join(returns_folder, f"{industry_event}_Expected_Return.csv")
            return_data.to_csv(output_file, index=False)
            print(f"Saved expected return to: {output_file}")
        else:
            print(f"Missing return file: {return_file}")
