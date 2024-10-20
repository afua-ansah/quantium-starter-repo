import pandas

df_0 = pandas.read_csv('./daily_sales_data_0.csv')
df_filtered_0 = df_0[df_0['product'] == 'pink morsel']
df_filtered_0.loc[:, 'sales'] = df_filtered_0['quantity'].astype(int) * df_filtered_0['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)
df_filtered_0['sales'] = df_filtered_0['sales'].apply(lambda x: f"${x:,.2f}")
df_final_0 = df_filtered_0[['sales', 'date', 'region']]

df_1 = pandas.read_csv('./daily_sales_data_1.csv')
df_filtered_1 = df_1[df_1['product'] == 'pink morsel']
df_filtered_1.loc[:, 'sales'] = df_filtered_1['quantity'].astype(int) * df_filtered_1['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)
df_filtered_1['sales'] = df_filtered_1['sales'].apply(lambda x: f"${x:,.2f}")
df_final_1 = df_filtered_1[['sales', 'date', 'region']]

df_2 = pandas.read_csv('./daily_sales_data_2.csv')
df_filtered_2 = df_2[df_2['product'] == 'pink morsel']
df_filtered_2.loc[:, 'sales'] = df_filtered_2['quantity'].astype(int) * df_filtered_2['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)
df_filtered_2['sales'] = df_filtered_2['sales'].apply(lambda x: f"${x:,.2f}")
df_final_2 = df_filtered_2[['sales', 'date', 'region']]

final_df = pandas.concat([df_final_0, df_final_1, df_final_2], ignore_index=True)
final_df.to_csv('processed_data.csv', index=False)

# Alternative Implementation
# import csv
# import os

# DATA_DIRECTORY = "./data"
# OUTPUT_FILE_PATH = "./formatted_data.csv"

# # open the output file
# with open(OUTPUT_FILE_PATH, "w") as output_file:
#     writer = csv.writer(output_file)

#     # add a csv header
#     header = ["sales", "date", "region"]
#     writer.writerow(header)

#     # iterate through all files in the data directory
#     for file_name in os.listdir(DATA_DIRECTORY):
#         # open the csv file for reading
#         with open(f"{DATA_DIRECTORY}/{file_name}", "r") as input_file:
#             reader = csv.reader(input_file)
#             # iterate through each row in the csv file
#             row_index = 0
#             for input_row in reader:
#                 # if this row is not the csv header, process it
#                 if row_index > 0:
#                     # collect data from row
#                     product = input_row[0]
#                     raw_price = input_row[1]
#                     quantity = input_row[2]
#                     transaction_date = input_row[3]
#                     region = input_row[4]

#                     # if this is a pink morsel transaction, process it
#                     if product == "pink morsel":
#                         # finish formatting data
#                         price = float(raw_price[1:])
#                         sale = price * int(quantity)

#                         # write the row to output file
#                         output_row = [sale, transaction_date, region]
#                         writer.writerow(output_row)
#                 row_index += 1