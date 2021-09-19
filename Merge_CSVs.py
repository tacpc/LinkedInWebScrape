import pandas as pd
import os
import glob

path = os.getcwd()
csv_files = glob.glob(os.path.join(path+'\\Scraped_Data', "*.csv"))

dfs = list()
for csv_file in csv_files:
    df = pd.read_csv(csv_file, sep=';')
    df['Filename'] = csv_file.split('\\')[-1]
    df['File_Date'] = csv_file.split('\\')[-1][:10]
    dfs.append(df)

merged_df = pd.concat(dfs,axis=0, ignore_index=True)

merged_df.to_csv(path+'\\Scraped_Data\\Merged_Data\\Merged_Data.csv', sep=',', index=False, header=True, encoding='UTF-8')