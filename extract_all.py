import numpy as np  # Ye line miss thi
import pandas as pd
from scipy.io import loadmat
import glob
import os

def process_all_files():
    all_files = glob.glob("data/*.mat")
    all_data = []

    for file in all_files:
        print(f"Processing: {file}")
        try:
            mat = loadmat(file)
            root_key = [k for k in mat.keys() if not k.startswith('__')][0]
            data_struct = mat[root_key]
            
            # NASA data structure traversal
            cycles = data_struct[0][0]['cycle'][0]
            
            for i, cycle in enumerate(cycles):
                type_val = cycle['type'][0]
                if isinstance(type_val, np.ndarray):
                    type_val = type_val[0]
                
                if type_val == 'discharge':
                    data = cycle['data'][0][0]
                    if 'Capacity' in data.dtype.names:
                        cap = data['Capacity'][0][0]
                        all_data.append({
                            'battery_id': os.path.basename(file),
                            'cycle_index': i,
                            'capacity': float(cap)
                        })
        except Exception as e:
            print(f"Skipping {file} due to structure: {e}")

    df = pd.DataFrame(all_data)
    df.to_csv('combined_battery_data.csv', index=False)
    print("\nSuccess! 'combined_battery_data.csv' generate ho gayi hai.")

if __name__ == "__main__":
    process_all_files()