# Netflix Movies and TV Shows – Exploratory Data Analysis (EDA)

An Exploratory Data Analysis project on the Netflix Movies and TV Shows dataset, developed as part of the **SWYNEX Internship – Task 2**. This project explores Netflix's content catalogue using Python, statistical analysis, and data visualization to identify patterns, trends, and insights.

## Project Overview

The objective of this project is to understand the distribution and characteristics of movies and TV shows available in the Netflix dataset. It explores content types, ratings, countries, genres, release years, movie durations, and TV show seasons.

The analysis also uses statistical techniques, correlation analysis, and outlier detection to uncover meaningful patterns in the dataset.

## Objectives

- Understand the structure and characteristics of the dataset.
- Identify missing values and duplicate records.
- Analyze the distribution of movies and TV shows.
- Explore content ratings, genres, countries, and release-year trends.
- Study movie durations and TV show seasons.
- Perform statistical analysis and correlation analysis.
- Detect outliers using the Interquartile Range (IQR) method.
- Present findings through visualizations and business insights.

## Dataset

**Dataset:** Netflix Movies and TV Shows

**Source:** [Kaggle – Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)

| Dataset information | Details |
|---|---|
| Total records | 8,807 |
| Total columns | 14 |
| Movies | 6,131 |
| TV Shows | 2,676 |
| Missing date-added values | 10 |
| Duplicate records | 0 |

The cleaned dataset includes information such as title, content type, director, cast, country, release year, rating, duration, genres, and description.

## Technologies Used

- **Python** – Programming language
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **SciPy** – Statistical analysis

## Project Structure

```text
SWYNEX-Exploratory-Data-Analysis/
│
├── data/
│   └── processed/
│       └── netflix_cleaned.csv
│
├── src/
│   ├── eda.py
│   ├── univariate_analysis.py
│   ├── bivariate_analysis.py
│   ├── statistical_analysis.py
│   └── advanced_eda.py
│
├── reports/
│   ├── figures/
│   ├── advanced_eda_summary.csv
│   ├── country_genre_analysis.csv
│   ├── statistical_summary.csv
│   ├── statistical_insights.md
│   └── final_eda_report.md
│
├── README.md
└── requirements.txt
```

## Analysis Performed

### 1. Data Exploration
- Dataset shape and structure
- Data types and descriptive statistics
- Missing-value analysis
- Duplicate detection

### 2. Univariate Analysis
- Movie vs TV show distribution
- Content rating distribution
- Top content-producing countries
- Release-year distribution
- Movie duration distribution
- TV show seasons distribution

### 3. Bivariate Analysis
- Content type vs release year
- Content type vs ratings
- Country vs content type
- Release decade vs average movie duration
- Content rating comparison using a heatmap

### 4. Statistical Analysis
- Mean, median, and mode
- Standard deviation and variance
- Quartiles and Interquartile Range (IQR)
- Skewness and kurtosis
- Box plots and distribution analysis

### 5. Advanced EDA
- Pearson and Spearman correlation
- Outlier detection using IQR
- Genre frequency analysis
- Content addition trends
- Country-wise genre analysis

## Key Findings

- Movies account for approximately **69.62%** of the dataset, while TV shows account
