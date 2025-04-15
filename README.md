This was a personal learning project to practice data cleaning, merging, and visualization using real-world entertainment data. It helped me apply sqlite, Python and, pandas in a meaningful way while exploring an interesting cultural topic.

# Netflix vs IMDb: How Do Netflix Titles Compare?
This project analyzes how titles available on **Netflix** compare to the **IMDb Top 1000 movies**, using Python and public datasets. The goal is to understand whether Netflix content tends to be rated lower, the same, or better than other popular titles.

## Tools Used

- Python
- pandas
- matplotlib
- sqlite3

## What the Project Does

1. Loads two real datasets (Netflix and IMDb)
2. Cleans and standardizes title and year columns
3. Merges Netflix content with IMDb Top 1000 entries
4. Analyzes IMDb rating distribution of Netflix vs non-Netflix content
5. Exports merged data to both CSV and SQLite database
6. Runs SQL validation queries on the database

## ✅ Key Findings

- 145 titles from IMDb’s Top 1000 were found on Netflix
- Average IMDb rating for:
  - Netflix titles: **8.00**
  - Non-Netflix titles: **7.94**
- Netflix content in the Top 1000 performs just as well or slightly better than other top-rated content
