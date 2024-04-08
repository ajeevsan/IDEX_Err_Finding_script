import pandas as pd

# Read the Excel file
df = pd.read_excel("cdh_pae_24hr.xlsx")

# List of error columns
error_columns = ['error(t-1)', 'error(t-2)', 'error(t-3)', 'error(t-4)', 'error(t-5)', 'error(t-6)', 
                'error(t-7)', 'error(t-8)', 'error(t-9)', 'error(t-10)', 'error(t-11)', 'error(t-12)', 
                'error(t-13)', 'error(t-14)', 'error(t-15)', 'error(t-16)', 'error(t-17)', 'error(t-18)', 
                'error(t-19)', 'error(t-20)', 'error(t-21)', 'error(t-22)', 'error(t-23)', 'error(t-24)']


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
