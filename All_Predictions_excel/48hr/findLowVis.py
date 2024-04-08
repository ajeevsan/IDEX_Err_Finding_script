import pandas as pd

# Read the Excel file
df = pd.read_excel("sng_pae_48hr.xlsx")

# List of error columns adjusted for intervals of 2 starting from t-2 to t-48
error_columns = ['error(t-2)', 'error(t-4)', 'error(t-6)', 'error(t-8)', 'error(t-10)', 'error(t-12)', 'error(t-14)', 
                'error(t-16)', 'error(t-18)', 'error(t-20)', 'error(t-22)', 'error(t-24)', 'error(t-26)', 'error(t-28)', 
                'error(t-30)', 'error(t-32)', 'error(t-34)', 'error(t-36)', 'error(t-38)', 'error(t-40)', 'error(t-42)', 
                'error(t-44)', 'error(t-46)', 'error(t-48)']

# Calculate percentage error including rows where actual is < 500 and is not 0 or -1
for column in error_columns:
    # df[column.replace("error", "Percentage_Error")] = df.apply(
    #     lambda row: (row[column] / row['actual(t)'] * 100
    #                  if row['actual(t)'] != 0 and row['actual(t)'] != -1 and row['actual(t)'] < 500
    #                  else 0), axis=1)
    # 
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
