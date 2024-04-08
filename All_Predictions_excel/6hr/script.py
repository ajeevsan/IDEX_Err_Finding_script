import pandas as pd

# Read the Excel file
df = pd.read_excel("sng_pae_6hr.xlsx")

# List of error columns
error_columns = ['error(t-0.5)', 'error(t-1.0)', 'error(t-1.5)', 'error(t-2.0)', 'error(t-2.5)', 
                 'error(t-3.0)', 'error(t-3.5)', 'error(t-4.0)', 'error(t-4.5)', 'error(t-5.0)', 
                 'error(t-5.5)', 'error(t-6.0)']

# Calculate percentage error and handle cases where actual value is 0 or -1
for column in error_columns:
    df[column.replace("error", "Percentage_Error")] = df.apply(lambda row: row[column] / row['actual(t)'] * 100 
                                                               if row['actual(t)'] not in [0, -1] else 0, axis=1)

# Calculate the average percentage error for each error column
average_percentage_errors = {}
for column in error_columns:
    average_percentage_errors[column] = df[column.replace("error", "Percentage_Error")].mean()

# Print the average percentage error for each error column
for column, avg_error in average_percentage_errors.items():
    print(f"Average Percentage Error for {column}: {avg_error}")

# Overall average percentage error
overall_avg_error = sum(average_percentage_errors.values()) / len(average_percentage_errors)
print("Overall Average Percentage Error:", overall_avg_error)
