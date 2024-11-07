import pandas as pd
from scipy.stats import chi2_contingency

# Load the data from the Excel file
file_path = 'Database.xlsx'
data = pd.read_excel(file_path)

# Initialize a list to store the results
results = []

# Iterate over all pairs of columns to perform Chi-Square test
for col1 in data.columns:
    for col2 in data.columns:
        if col1 != col2:
            # Create a contingency table with the frequencies of each combination
            contingency_table = pd.crosstab(data[col1], data[col2])
            
            # Perform the Chi-Square test on the contingency table
            chi2_stat, p_val, dof, expected = chi2_contingency(contingency_table)
            
            # Store the results in the list
            results.append({
                'Column 1': col1,
                'Column 2': col2,
                'Chi-Square Statistic': chi2_stat,
                'P-Value': p_val,
                'Degrees of Freedom': dof,
                'Expected Frequencies': expected
            })

# Convert the results to a DataFrame
results_df = pd.DataFrame(results)

# Save the results to a new Excel file
results_df.to_excel('chi_square_all_columns_results.xlsx', index=False)

print("Chi-Square test results for all column pairs have been saved to 'chi_square_all_columns_results.xlsx'.")


