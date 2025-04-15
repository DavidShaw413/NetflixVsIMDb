# -----------------------------------
# STEP 1: Import libraries and load data
# -----------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# File paths (make sure the CSV files are in the "Data" folder)
netflix_path = "Data/netflix_titles.csv"
imdb_path = "Data/imdb_top_1000.csv"

# Load the CSV files into DataFrames
netflix_df = pd.read_csv(netflix_path)
imdb_df = pd.read_csv(imdb_path)

# -----------------------------------
# STEP 2: Clean the data
# -----------------------------------

# Clean Netflix titles (remove extra spaces and lowercase)
netflix_df['title'] = netflix_df['title'].str.strip().str.lower()
# Make sure release_year is a number
netflix_df['release_year'] = pd.to_numeric(netflix_df['release_year'], errors='coerce')

# Clean IMDb titles (same process)
imdb_df['Series_Title'] = imdb_df['Series_Title'].str.strip().str.lower()
imdb_df['Released_Year'] = pd.to_numeric(imdb_df['Released_Year'], errors='coerce')

# -----------------------------------
# STEP 3: Merge both datasets
# -----------------------------------

# Join the two datasets based on title and release year
merged_df = pd.merge(
    netflix_df,
    imdb_df,
    left_on=['title', 'release_year'],
    right_on=['Series_Title', 'Released_Year'],
    how='inner'
)

# Show how many matches were found
print(f"Merged dataset: {len(merged_df)} matches found")
print(merged_df[['title', 'release_year', 'IMDB_Rating']].head())

# -----------------------------------
# STEP 4: Analyze the IMDb ratings for Netflix titles
# -----------------------------------

# Display summary statistics for IMDb ratings
print("IMDb Rating stats for matched Netflix titles:")
print(merged_df['IMDB_Rating'].describe())

# Show a histogram of IMDb ratings for Netflix titles
plt.figure(figsize=(8, 5))
plt.hist(merged_df['IMDB_Rating'], bins=10, edgecolor='black')
plt.title("Distribution of IMDb Ratings for Netflix Titles (in Top 1000)")
plt.xlabel("IMDb Rating")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------------
# STEP 5: Compare with non-Netflix IMDb titles
# -----------------------------------

# Get the set of titles that appear on Netflix + IMDb
netflix_titles_set = set(merged_df['Series_Title'])

# Filter IMDb titles that are not on Netflix
non_netflix_df = imdb_df[~imdb_df['Series_Title'].isin(netflix_titles_set)]

print(f"IMDb titles not on Netflix: {len(non_netflix_df)}")

# Plot ratings comparison between Netflix and non-Netflix titles
plt.figure(figsize=(10, 6))
plt.hist(merged_df['IMDB_Rating'], bins=10, alpha=0.7, label="On Netflix", edgecolor='black')
plt.hist(non_netflix_df['IMDB_Rating'], bins=10, alpha=0.7, label="Not on Netflix", edgecolor='black')
plt.title("IMDb Ratings: Netflix vs. Non-Netflix Titles in Top 1000")
plt.xlabel("IMDb Rating")
plt.ylabel("Number of Titles")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Print average ratings
print("Average IMDb Rating (Netflix):", round(merged_df['IMDB_Rating'].mean(), 2))
print("Average IMDb Rating (Non-Netflix):", round(non_netflix_df['IMDB_Rating'].mean(), 2))

# -----------------------------------
# STEP 6: Save merged data to CSV
# -----------------------------------

# Save the merged data to a new CSV in the Data folder
output_path = "Data/netflix_imdb_merged.csv"
merged_df.to_csv(output_path, index=False)

print(f"CSV saved to: {output_path}")
