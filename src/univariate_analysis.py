import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load dataset
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "netflix_cleaned.csv"

df = pd.read_csv(DATA_PATH)

# Create folder for visualizations
OUTPUT_DIR = PROJECT_ROOT / "reports" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")

# 1. Movies vs TV Shows
plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="type", hue="type",
              palette="Set2", legend=False)

plt.title("Distribution of Movies and TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "content_type_distribution.png")
plt.show()

# 2. Content Ratings Distribution
plt.figure(figsize=(12, 6))

rating_counts = df["rating"].value_counts()

sns.barplot(x=rating_counts.index, y=rating_counts.values,
            hue=rating_counts.index, palette="viridis",
            legend=False)

plt.title("Distribution of Netflix Content Ratings")
plt.xlabel("Content Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "content_ratings.png")
plt.show()

# 3. Top 10 Content Producing Countries
countries = (
    df["country"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)

countries = countries[~countries.isin(["Unknown", ""])]

top_countries = countries.value_counts().head(10)

plt.figure(figsize=(11, 6))

sns.barplot(x=top_countries.values,
            y=top_countries.index,
            hue=top_countries.index,
            palette="mako",
            legend=False)

plt.title("Top 10 Countries by Netflix Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_countries.png")
plt.show()

# 4. Release Year Distribution

plt.figure(figsize=(10, 5))

sns.histplot(data=df, x="release_year",
             bins=30, kde=True)

plt.title("Netflix Content Release Year Distribution")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "release_year_distribution.png")
plt.show()


# 5. Movie Duration Distribution

movies = df[df["type"] == "Movie"].copy()

plt.figure(figsize=(10, 5))

sns.histplot(data=movies, x="duration_value",
             bins=30, kde=True)

plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "movie_duration_distribution.png")
plt.show()


# 6. TV Show Seasons Distribution

tv_shows = df[df["type"] == "TV Show"].copy()

plt.figure(figsize=(9, 5))

sns.countplot(data=tv_shows, x="duration_value",
              hue="duration_value",
              palette="Set2",
              legend=False)

plt.title("Distribution of TV Show Seasons")
plt.xlabel("Number of Seasons")
plt.ylabel("Number of TV Shows")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "tv_seasons_distribution.png")
plt.show()


print("\n========== UNIVARIATE ANALYSIS COMPLETE ==========")

print("\nContent Type Counts:")
print(df["type"].value_counts())

print("\nTop 10 Ratings:")
print(rating_counts.head(10))

print("\nTop 10 Countries:")
print(top_countries)

print("\nMovie Duration Statistics:")
print(movies["duration_value"].describe())

print("\nTV Show Season Statistics:")
print(tv_shows["duration_value"].describe())

print("\nAll charts saved in reports/figures/")
