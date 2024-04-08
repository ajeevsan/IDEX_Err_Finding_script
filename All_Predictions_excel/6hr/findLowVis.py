import pandas as pd

# Read the Excel file
df = pd.read_excel("cdh_pae_6hr.xlsx")

# List of error columns adjusted for intervals of 2 starting from t-2 to t-48
error_columns = ['error(t-0.5)', 'error(t-1.0)', 'error(t-1.5)', 'error(t-2.0)', 'error(t-2.5)', 
                 'error(t-3.0)', 'error(t-3.5)', 'error(t-4.0)', 'error(t-4.5)', 'error(t-5.0)', 
                 'error(t-5.5)', 'error(t-6.0)']

# Calculate percentage error including rows where actual is < 500 and is not 0 or -1
for column in error_columns:
    # df[column.replace("error", "Percentage_Error")] = df.apply(
    #     lambda row: (row[column] / row['actual(t)'] * 100
    #                  if row['actual(t)'] != 0 and row['actual(t)'] != -1 and row['actual(t)'] < 500
    #                  else 0), axis=1)
    
    # df[column.replace("error", "Percentage_Error")] = df.apply(
    #     lambda row: (row[column] / row['actual(t)'] * 100
    #                  if row['actual(t)'] != 0 and row['actual(t)'] != -1 and row['actual(t)'] > 500 and row['actual(t)'] < 1000
    #                  else 0), axis=1)
    
    # df[column.replace("error", "Percentage_Error")] = df.apply(
    #     lambda row: (row[column] / row['actual(t)'] * 100
    #                  if row['actual(t)'] != 0 and row['actual(t)'] != -1 and row['actual(t)'] > 1000 and row['actual(t)'] < 1500
    #                  else 0), axis=1)
    
    # df[column.replace("error", "Percentage_Error")] = df.apply(
    #     lambda row: (row[column] / row['actual(t)'] * 100
    #                  if row['actual(t)'] != 0 and row['actual(t)'] != -1 and row['actual(t)'] > 1500
    #                  else 0), axis=1)
    
    df[column.replace("error", "Percentage_Error")] = df.apply(
        lambda row: (row[column] / row['actual(t)'] * 100
                     if row['actual(t)'] != 0 and row['actual(t)'] != -1
                     else 0), axis=1)

# Calculate the average percentage error for each error column, considering all non-None values
average_percentage_errors = {}
for column in error_columns:
    # Filter out None values before calculating the mean to avoid including rows with actual >= 500 or actual == 0
    filtered_errors = df[df[column.replace("error", "Percentage_Error")].notna()][column.replace("error", "Percentage_Error")]
    average_percentage_errors[column] = filtered_errors.mean()

# Print the average percentage error for each error column
for column, avg_error in average_percentage_errors.items():
    print(f"Average Percentage Error for {column}: {avg_error}")

# Calculate the overall average percentage error, considering all non-None values
all_errors = pd.concat([df[col] for col in df.columns if "Percentage_Error" in col and df[col].notna().any()], axis=0)
overall_avg_error = all_errors.mean()

print(f"Overall Average Percentage Error: {overall_avg_error}")
