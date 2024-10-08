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
print(final_df.head)