
# ==========================================================
# SWYNEX INTERNSHIP - TASK 2
# ADVANCED EXPLORATORY DATA ANALYSIS
# Dataset: Netflix Movies and TV Shows
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ----------------------------------------------------------
# 1. PROJECT CONFIGURATION
# ----------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data" / "processed" / "netflix_cleaned.csv"

OUTPUT_DIR = PROJECT_ROOT / "reports" / "figures"
REPORT_DIR = PROJECT_ROOT / "reports"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")

df = pd.read_csv(DATA_PATH)

print("\nDataset loaded successfully!")
print("Dataset Shape:", df.shape)


# ----------------------------------------------------------
# 2. CORRELATION ANALYSIS
# Movie Release Year vs Movie Duration
# ----------------------------------------------------------

print("\n1. Performing Correlation Analysis...")

movies = df[df["type"] == "Movie"].copy()

correlation_data = movies[
    ["release_year", "duration_value"]
].dropna()

pearson_corr = correlation_data[
    "release_year"
].corr(correlation_data["duration_value"], method="pearson")

spearman_corr = correlation_data[
    "release_year"
].corr(correlation_data["duration_value"], method="spearman")

print("\nPearson Correlation:", round(pearson_corr, 3))
print("Spearman Correlation:", round(spearman_corr, 3))

plt.figure(figsize=(10, 6))

sns.regplot(
    data=correlation_data,
    x="release_year",
    y="duration_value",
    scatter_kws={"alpha": 0.3},
    line_kws={"color": "red"}
)

plt.title("Relationship Between Movie Release Year and Duration")
plt.xlabel("Release Year")
plt.ylabel("Movie Duration (Minutes)")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "correlation_analysis.png", dpi=300)
plt.close()


# ----------------------------------------------------------
# 3. OUTLIER DETECTION USING IQR
# ----------------------------------------------------------

print("\n2. Performing Outlier Detection...")

def detect_outliers(series):

    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    iqr = q3 - q1

    lower_limit = q1 - (1.5 * iqr)
    upper_limit = q3 + (1.5 * iqr)

    outliers = series[
        (series < lower_limit) |
        (series > upper_limit)
    ]

    return {
        "Q1": q1,
        "Q3": q3,
        "IQR": iqr,
        "Lower Limit": lower_limit,
        "Upper Limit": upper_limit,
        "Outlier Count": len(outliers)
    }


movie_outliers = detect_outliers(
    movies["duration_value"]
)

tv_shows = df[df["type"] == "TV Show"].copy()

tv_outliers = detect_outliers(
    tv_shows["duration_value"]
)

print("\nMovie Duration Outliers:")
print(movie_outliers)

print("\nTV Show Season Outliers:")
print(tv_outliers)


# Movie duration boxplot

plt.figure(figsize=(10, 5))

sns.boxplot(
    x=movies["duration_value"],
    color="skyblue"
)

plt.title("Outlier Detection in Movie Durations")
plt.xlabel("Movie Duration (Minutes)")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "advanced_movie_outliers.png", dpi=300)
plt.close()


# TV show seasons boxplot

plt.figure(figsize=(10, 5))

sns.boxplot(
    x=tv_shows["duration_value"],
    color="lightgreen"
)

plt.title("Outlier Detection in TV Show Seasons")
plt.xlabel("Number of Seasons")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "advanced_tv_outliers.png", dpi=300)
plt.close()


# ----------------------------------------------------------
# 4. GENRE ANALYSIS
# ----------------------------------------------------------

print("\n3. Performing Genre Analysis...")

genres = (
    df["listed_in"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)

genre_counts = genres.value_counts()

top_genres = genre_counts.head(10)

print("\nTop 10 Netflix Genres:")
print(top_genres)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_genres.values,
    y=top_genres.index,
    hue=top_genres.index,
    palette="viridis",
    legend=False
)

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_genres.png", dpi=300)
plt.close()


# ----------------------------------------------------------
# 5. CONTENT ADDITION TRENDS
# ----------------------------------------------------------

print("\n4. Analysing Content Addition Trends...")

df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

df["added_year"] = df["date_added"].dt.year

addition_trends = (
    df["added_year"]
    .dropna()
    .value_counts()
    .sort_index()
)

print("\nNetflix Content Addition by Year:")
print(addition_trends)

plt.figure(figsize=(11, 6))

sns.lineplot(
    x=addition_trends.index,
    y=addition_trends.values,
    marker="o"
)

plt.title("Netflix Content Addition Trends by Year")
plt.xlabel("Year Added to Netflix")
plt.ylabel("Number of Titles Added")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "content_addition_trends.png", dpi=300)
plt.close()


# ----------------------------------------------------------
# 6. COUNTRY VS GENRE ANALYSIS
# ----------------------------------------------------------

print("\n5. Analysing Country vs Genre...")

country_genre = df[
    ["country", "listed_in"]
].dropna().copy()

country_genre["country"] = (
    country_genre["country"].str.split(",")
)

country_genre["listed_in"] = (
    country_genre["listed_in"].str.split(",")
)

country_genre = country_genre.explode("country")

country_genre = country_genre.explode("listed_in")

country_genre = country_genre.reset_index(drop=True)

country_genre["country"] = (
    country_genre["country"].str.strip()
)

country_genre["listed_in"] = (
    country_genre["listed_in"].str.strip()
)

country_genre = country_genre[
    (country_genre["country"] != "")
    & (country_genre["listed_in"] != "")
    & (country_genre["country"] != "Unknown")
].copy()

top_countries = (
    df["country"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
    .head(5)
    .index
)

filtered_country_genre = country_genre[
    country_genre["country"].isin(top_countries)
]

country_genre_table = pd.crosstab(
    filtered_country_genre["country"],
    filtered_country_genre["listed_in"]
)

# Save country genre data
country_genre_table.to_csv(
    REPORT_DIR / "country_genre_analysis.csv"
)

print("\nCountry vs Genre Table:")
print(country_genre_table)

# Heatmap of the most common genres
common_genres = genres.value_counts().head(8).index

heatmap_data = country_genre_table.reindex(
    columns=common_genres,
    fill_value=0
)

plt.figure(figsize=(13, 7))

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt="d",
    cmap="YlGnBu",
    linewidths=0.5
)

plt.title("Top Genres Across Top 5 Countries")
plt.xlabel("Genre")
plt.ylabel("Country")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "country_genre_heatmap.png", dpi=300)
plt.close()


# ----------------------------------------------------------
# 7. SAVE ANALYSIS RESULTS
# ----------------------------------------------------------

advanced_summary = pd.DataFrame({
    "Analysis": [
        "Pearson Correlation",
        "Spearman Correlation",
        "Movie Duration Outliers",
        "TV Show Season Outliers",
        "Total Genres"
    ],
    "Result": [
        pearson_corr,
        spearman_corr,
        movie_outliers["Outlier Count"],
        tv_outliers["Outlier Count"],
        len(genre_counts)
    ]
})

advanced_summary.to_csv(
    REPORT_DIR / "advanced_eda_summary.csv",
    index=False
)


# ----------------------------------------------------------
# 8. FINAL OUTPUT
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("       ADVANCED EDA COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nFiles saved in reports/figures:")
print("1. correlation_analysis.png")
print("2. advanced_movie_outliers.png")
print("3. advanced_tv_outliers.png")
print("4. top_genres.png")
print("5. content_addition_trends.png")
print("6. country_genre_heatmap.png")

print("\nAdditional reports:")
print("1. advanced_eda_summary.csv")
print("2. country_genre_analysis.csv")

print("\nAll analyses completed!")
