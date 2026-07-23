import pandas as pd

# Path to the combined output file
input_file = r"C:/Users/marco/OneDrive/Escritorio/Event_Analysis_Output/industry_event_30day_returns.csv"

# Read the combined data
df = pd.read_csv(input_file)

# Get the list of unique events
events = df['Event'].unique()

# Output folder for the split files
output_folder = r"C:/Users/marco/OneDrive/Escritorio/Event_Analysis_Output"

# Loop through each event and split the data
for event in events:
    # Filter the data for the current event
    event_df = df[df['Event'] == event]
    
    # Create a file name for the event
    event_file_name = f"{event.replace(' ', '_')}_30day_returns.csv"
    
    # Save the filtered DataFrame to a CSV file
    event_df.to_csv(f"{output_folder}/{event_file_name}", index=False)
    
    print(f"File created for event: {event} at {output_folder}/{event_file_name}")

print("All files split and saved successfully!")
