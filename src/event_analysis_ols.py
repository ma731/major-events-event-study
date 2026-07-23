import pandas as pd
import statsmodels.api as sm
import os

# Data root: original absolute paths replaced with a configurable root.
# Point EVENT_STUDY_DATA at the folder holding OLS/, UK Result/,
# Event_Analysis_Output/, etc. Defaults to <repo>/data.
DATA_ROOT = os.environ.get(
    "EVENT_STUDY_DATA",
    os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")))


events = {
    "Donald Trump Reelection": "2024-11-06",
    "Covid-19 Pandemic Lockdown in CN": "2020-01-23",
    "Brexit Referendum Day": "2016-06-23",
    "Start of Russia's Annexation of Ukraine": "2022-02-24",
    "Global Financial Crisis": "2008-09-15"
}

folders = [
    DATA_ROOT + "/UK Result/Transportation_and_Infrastructure",
    DATA_ROOT + "/UK Result/Agriculture_and_Food",
    DATA_ROOT + "/UK Result/Automotive",
    DATA_ROOT + "/UK Result/Defense_and_Aerospace",
    DATA_ROOT + "/UK Result/Energy_and_Utilities",
    DATA_ROOT + "/UK Result/Finance_and_Insurance",
    DATA_ROOT + "/UK Result/Healthcare_and_Pharmaceuticals",
    DATA_ROOT + "/UK Result/Manufacturing_and_Industrial_Goods",
    DATA_ROOT + "/UK Result/Real_Estate_and_Construction",
    DATA_ROOT + "/UK Result/Retail_and_Consumer_Goods",
    DATA_ROOT + "/UK Result/Technology_and_Telecommunications"
]

def read_data(folder):
    print(f"Reading data from folder: {folder}")
    files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    all_data = []
    for file in files:
        df = pd.read_csv(os.path.join(folder, file))
        all_data.append(df)
    data = pd.concat(all_data)
    print(f"Read {len(data)} rows from {len(files)} files.")
    return data

def perform_ols(data, event_date):
    print(f"Performing OLS regression for event date: {event_date}")
    # Convert Date to datetime and filter for 120 days before the event
    data['Date'] = pd.to_datetime(data['Date'])
    event_date = pd.to_datetime(event_date)
    start_date = event_date - pd.Timedelta(days=120)
    data_filtered = data[data['Date'] >= start_date]

    X = data_filtered['Market_Return']
    Y = data_filtered['Return']
    
    X = sm.add_constant(X)

    model = sm.OLS(Y, X).fit()

    results = pd.DataFrame({
        "Alpha": [model.params.iloc[0]],           
        "Beta": [model.params.iloc[1]],            
        "R-squared": [model.rsquared],
        "p-value": [model.pvalues.iloc[1]],         
        "Standard Error": [model.bse.iloc[1]],      
        "Adjusted R-squared": [model.rsquared_adj]
    })
    print(f"OLS regression results: \n{results}\n")
    return results

for folder in folders:
    folder_data = read_data(folder)
    for event_name, event_date in events.items():
        ols_results = perform_ols(folder_data, event_date)
        output_file = f"{folder}_{event_name}.csv"
        ols_results.to_csv(output_file, index=False)
        print(f"Results saved to: {output_file}")
