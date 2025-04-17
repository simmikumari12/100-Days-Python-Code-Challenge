import pandas as pd
import numpy as np
import random

# Excercise 1

# Create two series with random integers
ages = np.random.randint(0, 100, size=10)
scores = np.random.randint(0, 25, size=10)

# Create the DataFrame
df = pd.DataFrame({
    'age': ages,
    'score': scores
})

# Display the tail of the DataFrame
print("Tail of the DataFrame:")
print(df.tail())

# Use describe() to get basic statistics
print("\nBasic Statistics (describe):")
print(df.describe())

# Sort the DataFrame by 'score'
df_sorted = df.sort_values(by='score')
print("\nDataFrame sorted by 'score':")
print(df_sorted)


# Excercise 2

# Save DataFrame to CSV file
df.to_csv('pd_exer.csv', index=False)

# Read the DataFrame from the CSV file
df_loaded = pd.read_csv('pd_exer.csv')

# Display the loaded DataFrame
print("DataFrame read from 'pd_exer.csv':")
print(df_loaded)

# Excercise 3

# Add a new row to the bottom

new_row = {
    'age': np.random.randint(0, 100),
    'score': np.random.randint(0, 25)
}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)


# Insert 'company' column at the first index

companies = ['Google', 'Apple', 'Microsoft']
company_column = [random.choice(companies) for _ in range(len(df))]
df.insert(0, 'company', company_column)

# Show the updated DataFrame
print("Updated DataFrame with new row and 'company' column:")
print(df)

# Excercise 4

# Filter: score > 50
high_scores = df[df['score'] > 50]
print("Rows with score > 50:")
print(high_scores)

# Filter: score > 50 and age > 20
high_scores_and_age = df[(df['score'] > 50) & (df['age'] > 20)]
print("\nRows with score > 50 and age > 20:")
print(high_scores_and_age)

# Excercise 5

# Group the DataFrame by 'company'
grouped = df.groupby('company')

# Print info about each group
print("Group Information:")
for name, group in grouped:
    print(f"\nCompany: {name}")
    print(group)

# Aggregate for Apple group only
apple_group = grouped.get_group('Apple')

# Calculate median age and mean score for Apple group
apple_stats = apple_group.agg({
    'age': 'median',
    'score': 'mean'
})

print("\nAggregated statistics for Apple group:")
print(apple_stats)


# Excercise 6

# Calculate mean for 'age' and 'score' using apply
mean_values = df[['age', 'score']].apply(np.mean)

print("Mean values using apply():")
print(mean_values)

# Save the DataFrame again (with any changes you’ve made)
df.to_csv('pd_exer_final.csv', index=False)

print("\nCSV file 'pd_exer_final.csv' is ready for upload to iCollege.")
