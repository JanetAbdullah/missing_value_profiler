# Missing Value Profiler

This project performs a deep and structured analysis of missing values in a dataset. It helps Data Scientists identify not only which columns are incomplete, but also how missing data patterns relate across the dataset. It is ideal for understanding data quality issues before modeling or imputation.

## Project Objectives
- Report percentage of missing values per column
- Explore row-level missing value distribution
- Identify common missingness patterns (column combinations)
- Visualize co-occurrence of nulls between columns
- Support better imputation planning or data exclusion

## Features
- Synthetic dataset generation with conditional missingness
- Top 5 most frequent null patterns (as binary vectors)
- Heatmap of nulls in dataset
- Row-wise histogram of null counts
- Co-occurrence heatmap (which columns are missing together)

## Technologies Used
- Python 3.x
- pandas
- numpy
- seaborn
- matplotlib
- itertools

## How to Run
```bash
pip install pandas numpy seaborn matplotlib
python missing_value_profiler.py
```

## File Structure
```
missing_value_profiler/
├── missing_value_profiler.py   # Main script
├── README.md                   # Project documentation
```

## Visual Outputs
- Heatmap of missing entries
- Histogram of missing values per row
- Co-occurrence matrix of missing columns

## Key Insights
- Columns with over 30% missing may need imputation or exclusion
- Null co-occurrence can indicate dependent or systematic missingness
- Frequent patterns of nulls help inform targeted preprocessing

## Author
Janet Abdullah  
GitHub: [https://github.com/JanetAbdullah]  
Feel free to fork and adapt for profiling missing data in your own datasets.