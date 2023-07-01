import csv

def save_data(data):
    # Save the data to a CSV file
    filename = 'output.csv'
    fieldnames = ['col1', 'col2', 'col3']  # Replace with actual field names
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
