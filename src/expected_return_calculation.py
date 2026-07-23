import os
import pandas as pd

# Define the base directory for your files
base_dir = "C:/Users/marco/OneDrive/Escritorio/"

# List of directories and corresponding event sub-directories
industries = [
    "Agriculture and Food", "Automotive", "Defense and Aerospace", 
    "Energy and Utilities", "Finance and Insurance", "Healthcare and Pharmaceuticals", 
    "Manufacturing and Industrial Goods", "Real Estate and Construction", 
    "Retail and Consumer Goods", "Technology and Telecommunications", 
    "Transportation and Infrastructure"
]

events = [
    "Brexit_Referendum_Day", "Covid_19_Pandemic_Lockdown_in_CN", 
    "Donald_Trump_Reelection", "Global_Financial_Crisis", 
    "Start_of_Russia's_full_on_annexation_of_Ukraine"
]

# Function to generate file paths for each industry and event
def generate_event_file_paths():
    event_file_paths = []
    for industry in industries:
        for event in events:
            event_file_paths.append(
                os.path.join(base_dir, f"Industry_Event_Split/{industry}_{event}.csv")
            )
    return event_file_paths

# Generate the event file paths dynamically
event_file_paths = generate_event_file_paths()

# Define a function to process the CSV files
def process_files(file_paths):
    all_data = []
    
    for file_path in file_paths:
        if os.path.exists(file_path):
            try:
                # Read the CSV file
                data = pd.read_csv(file_path)
                # Process the data (this part can be customized based on your needs)
                data['file_name'] = os.path.basename(file_path)  # Adding a column with the file name
                all_data.append(data)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
        else:
            print(f"File not found: {file_path}")
    
    # Combine all the data into a single DataFrame (if needed)
    return pd.concat(all_data, ignore_index=True) if all_data else pd.DataFrame()

# Process all the files
processed_data = process_files(event_file_paths)

# You can now analyze `processed_data` or save it to a new CSV
processed_data.to_csv("processed_data.csv", index=False)
