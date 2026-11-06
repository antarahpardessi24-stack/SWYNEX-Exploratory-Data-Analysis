# Exploratory Data Analysis (EDA) – Netflix Movies and TV Shows

**Internship:** SWYNEX  
**Task:** Task 2 – Exploratory Data Analysis  
**Dataset:** Netflix Movies and TV Shows  
**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn  
**Project Type:** Data Analytics

---

## 1. Introduction

Exploratory Data Analysis (EDA) is an important process in data analytics that helps understand datasets, identify patterns, discover relationships and extract meaningful insights.

In this project, the Netflix Movies and TV Shows dataset is analysed to understand the distribution of content, ratings, genres, countries, release years and movie durations.

The objective is to discover useful patterns and generate business insights that can help understand Netflix's content catalogue.

## 2. Project Objectives

- Understand the structure of the Netflix dataset.
- Perform descriptive statistical analysis.
- Analyse numerical and categorical variables.
- Identify relationships between different variables.
- Detect outliers and unusual patterns.
- Create meaningful data visualizations.
- Extract business insights and recommendations.

## 3. Dataset Description

The Netflix dataset contains information about movies and television shows available on Netflix.

**Dataset statistics:**
- Total records: 8,807
- Total columns: 14
- Movies: 6,131
- TV Shows: 2,676
- Duplicate records: 0
- Missing values in date_added: 10

Important attributes include:
- show_id
- type
- title
- director
- cast
- country
- date_added
- release_year
- rating
- duration
- listed_in
- description
- duration_value
- duration_unit

## 4. Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Programming |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| VS Code | Development environment |
| GitHub | Version control and project hosting |

## 5. Methodology

The project followed these stages:

1. Dataset loading and inspection.
2. Understanding data types and missing values.
3. Univariate analysis.
4. Bivariate analysis.
5. Descriptive statistical analysis.
6. Correlation analysis.
7. Outlier detection using IQR.
8. Genre and country analysis.
9. Content addition trend analysis.
10. Business insight generation.

## 6. Univariate Analysis

Univariate analysis was performed to understand individual variables.

The following visualizations were created:

1. Movies vs TV Shows distribution.
2. Content ratings distribution.
3. Top 10 content-producing countries.
4. Release year distribution.
5. Movie duration distribution.
6. TV show seasons distribution.

**Key observations:**

- Movies represent approximately 69.62% of the catalogue.
- TV Shows represent approximately 30.38%.
- The United States is the leading country by title associations.
- India is another major contributor.
- Most movies have durations around 90–100 minutes.
- Most TV shows have one or two seasons.

## 7. Bivariate Analysis

Bivariate analysis was conducted to understand relationships between two variables.

The following comparisons were performed:

- Content Type vs Release Year
- Content Type vs Content Rating
- Country vs Content Type
- Release Decade vs Movie Duration
- Rating vs Content Type

**Key observations:**

- Movies have higher representation than TV Shows among titles released from 2000 onward.
- TV-MA is the most common rating for both content types.
- India has substantially more movie than TV Show title associations.
- Japan and South Korea have comparatively stronger TV Show representation.
- Average movie duration decreases across the release decades represented in the dataset.

## 8. Statistical Analysis

Descriptive statistics were calculated separately for movie duration and TV show seasons.

### Movie Duration

| Measure | Value |
|---|---:|
| Mean | 99.56 minutes |
| Median | 98 minutes |
| Mode | 90 minutes |
| Standard Deviation | 28.29 |
| Minimum | 3 minutes |
| Maximum | 312 minutes |
| IQR | 27 minutes |

### TV Show Seasons

| Measure | Value |
|---|---:|
| Mean | 1.76 seasons |
| Median | 1 season |
| Mode | 1 season |
| Standard Deviation | 1.58 |
| Minimum | 1 season |
| Maximum | 17 seasons |
| IQR | 1 season |

**Key observations:**

- The average movie duration is approximately 100 minutes.
- Most TV shows have one season.
- TV show season counts are strongly right-skewed.
- Movie durations have a much less skewed distribution.

## 9. Advanced Exploratory Data Analysis

Advanced analysis was conducted to identify deeper patterns.

### 9.1 Correlation Analysis

Pearson correlation: -0.206

Spearman correlation: -0.191

Both values indicate a weak negative relationship between movie release year and duration.

### 9.2 Outlier Detection

The Interquartile Range (IQR) method was used.

- Movie duration outliers: 450
- TV show season outliers: 259

These observations are statistical outliers and are not necessarily data errors.

### 9.3 Genre Analysis

The most frequently represented genres include:

| Genre | Title associations |
|---|---:|
| International Movies | 2,752 |
| Dramas | 2,427 |
| Comedies | 1,674 |
| International TV Shows | 1,351 |
| Documentaries | 869 |
| Action & Adventure | 859 |

### 9.4 Content Addition Trends

The highest number of Netflix content additions in the dataset occurred in 2019, with 2,016 titles.

Content additions increased considerably between 2015 and 2019, followed by a decline through 2021.

### 9.5 Country and Genre Analysis

A country-versus-genre comparison was performed using a heatmap to explore differences in genre representation across major content-producing countries.

## 10. Major Business Insights

Based on the analysis, the following insights were identified:

**Insight 1: Movie Dominance**

Movies account for approximately 69.62% of the Netflix catalogue, indicating a larger representation than TV Shows.

**Insight 2: Mature Content Representation**

TV-MA is the most common rating for both content types. It represents 42.79% of TV Shows and 33.63% of Movies.

**Insight 3: Regional Content Distribution**

The United States has the highest number of country-title associations, followed by India and the United Kingdom.

**Insight 4: Movie Duration Patterns**

The average movie duration is approximately 99.56 minutes, with most durations concentrated between 87 and 114 minutes.

**Insight 5: TV Show Season Patterns**

Most TV Shows have one season, while a smaller proportion have many seasons.

**Insight 6: Genre Representation**

International Movies, Dramas and Comedies are among the most frequently represented genres.

**Insight 7: Release Year and Duration**

A weak negative correlation exists between movie release year and duration.

**Insight 8: Content Addition Trends**

Netflix content additions peaked in 2019 within the available dataset.

## 11. Business Recommendations

Based on the findings, the following recommendations can be considered:

1. Develop personalized recommendations using genre, content rating and duration.
2. Analyse regional preferences to support localized content strategies.
3. Explore opportunities to expand content categories based on audience engagement.
4. Use release year and duration as additional recommendation features.
5. Study long-running TV Shows separately to understand their characteristics.
6. Monitor content addition patterns to support catalogue planning.

These are potential recommendations based on catalogue analysis; actual business decisions would require viewer engagement and performance data.

## 12. Conclusion

This Exploratory Data Analysis project provided a detailed understanding of Netflix's Movies and TV Shows catalogue.

Through univariate, bivariate, statistical and advanced analysis, several patterns were identified in content distribution, ratings, genres, countries, release years and durations.

The project demonstrated how Python libraries such as Pandas, NumPy, Matplotlib and Seaborn can be used to analyse data, create visualizations and extract meaningful business insights.

Overall, the analysis highlights the importance of EDA in understanding data and supporting data-driven decision-making.

---

**Project completed as part of SWYNEX Internship – Task 2: Exploratory Data Analysis.**