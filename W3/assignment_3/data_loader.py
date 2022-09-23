import csv # necessary for reading the csv file

def load_data_from_csv(filepath):
    
    rows = []
    
    with open(filepath, 'r') as rf:
        reader = csv.reader(rf)
        
        for row in reader:
            rows.append(row)
        
    # Separate headers and data
    headers = rows[0]
    data = rows[1:]
    
    return data, headers
