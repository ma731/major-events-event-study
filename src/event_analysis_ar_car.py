import os
import pandas as pd

# Define paths for OLS files
ols_paths = {
    "Transportation_and_Infrastructure": r"C:\Users\marco\OneDrive\Escritorio\OLS\Transportation and Infrastructure",
    "Agriculture_and_Food": r"C:\Users\marco\OneDrive\Escritorio\OLS\Agriculture and Food",
    "Automotive": r"C:\Users\marco\OneDrive\Escritorio\OLS\Automotive",
    "Defense_and_Aerospace": r"C:\Users\marco\OneDrive\Escritorio\OLS\Defense and Aerospace",
    "Energy_and_Utilities": r"C:\Users\marco\OneDrive\Escritorio\OLS\Energy and Utilities",
    "Finance_and_Insurance": r"C:\Users\marco\OneDrive\Escritorio\OLS\Finance and Insurance",
    "Healthcare_and_Pharmaceuticals": r"C:\Users\marco\OneDrive\Escritorio\OLS\Healthcare and Pharmaceuticals",
    "Manufacturing_and_Industrial_Goods": r"C:\Users\marco\OneDrive\Escritorio\OLS\Manufacturing and Industrial Goods",
    "Real_Estate_and_Construction": r"C:\Users\marco\OneDrive\Escritorio\OLS\Real Estate and Construction",
    "Retail_and_Consumer_Goods": r"C:\Users\marco\OneDrive\Escritorio\OLS\Retail and Consumer Goods",
    "Technology_and_Telecommunications": r"C:\Users\marco\OneDrive\Escritorio\OLS\Technology and Telecommunications"
}

# Define paths for event folders
event_folders = {
    "Start_of_Russia's_Annexation_of_Ukraine": r"C:\Users\marco\OneDrive\Escritorio\Split_By_Industry\Start_of_Russia's_Annexation_of_Ukraine",
    "Brexit_Referendum_Day": r"C:\Users\marco\OneDrive\Escritorio\Split_By_Industry\Brexit_Referendum_Day",
    "Covid-19_Pandemic_Lockdown_in_CN": r"C:\Users\marco\OneDrive\Escritorio\Split_By_Industry\Covid_19_Pandemic_Lockdown_in_CN",
    "Donald_Trump_Reelection": r"C:\Users\marco\OneDrive\Escritorio\Split_By_Industry\Donald_Trump_Reelection",
    "Global_Financial_Crisis": r"C:\Users\marco\OneDrive\Escritorio\Split_By_Industry\Global_Financial_Crisis"
}

# Output folder
output_folder = r"C:\Users\marco\OneDrive\Escritorio\Event_Analysis_Output\Expected_Returns"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to extract alpha and beta from OLS files
def extract_alpha_beta(ols_path, industry, event_name):
    file_name = f"{industry}_{event_name}.csv"
    file_path = os.path.join(ols_path, file_name)
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        if 'Alpha' in df.columns and 'Beta' in df.columns:
            alpha = df['Alpha'].iloc[0]
            beta = df['Beta'].iloc[0]
            return alpha, beta
        else:
            print(f"Alpha or Beta columns missing in {file_path}")
    else:
        print(f"OLS file not found: {file_name}")
    return None, None

# Function to calculate expected return
def calculate_expected_return(event_file_path, alpha, beta):
    if os.path.exists(event_file_path):
        df = pd.read_csv(event_file_path)
        if 'Market_Return' in df.columns:
            # Calculate Expected Return
            df['Expected_Return'] = alpha + (beta * df['Market_Return'])
            return df
        else:
            print(f"Market_Return column missing in {event_file_path}")
    else:
        print(f"Event file not found: {event_file_path}")
    return None

# Main process to calculate expected returns
for event_name, event_folder in event_folders.items():
    for industry, ols_path in ols_paths.items():
        event_file_path = os.path.join(event_folder, f"{industry}_{event_name}.csv")
        # Extract Alpha and Beta for the industry and event
        alpha, beta = extract_alpha_beta(ols_path, industry, event_name)
        if alpha is not None and beta is not None:
            # Calculate Expected Return for the event
            expected_return_df = calculate_expected_return(event_file_path, alpha, beta)
            if expected_return_df is not None:
                # Save the output to a CSV
                output_file = os.path.join(output_folder, f"{industry}_{event_name}_Expected_Returns.csv")
                expected_return_df.to_csv(output_file, index=False)
                print(f"Expected returns saved to: {output_file}")
