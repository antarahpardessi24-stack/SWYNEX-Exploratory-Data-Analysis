
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ----------------------------------------------------------
# 1. PROJECT CONFIGURATION
# ----------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data" / "processed" / "netflix_cleaned.csv"

OUTPUT_DIR = PROJECT_ROOT / "reports" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid", palette="Set2")

df = pd.read_csv(DATA_PATH)

print("\nDataset loaded successfully!")
print("Dataset Shape:", df.shape)


# ----------------------------------------------------------
# 2. CONTENT TYPE VS RELEASE YEAR
# ----------------------------------------------------------

print("\n1. Analysing Content Type vs Release Year...")

year_type = (
    df[df["release_year"] >= 2000]
    .groupby(["release_year", "type"])
    .size()
    .reset_index(name="count")
)

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=year_type,
    x="release_year",
    y="count",
    hue="type",
    marker="o"
)

plt.title("Release Year Trends: Movies vs TV Shows")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "type_vs_release_year.png", dpi=300)
plt.close()


# ----------------------------------------------------------
# 3. CONTENT TYPE VS CONTENT RATING
# ----------------------------------------------------------

print("2. Analysing Content Type vs Content Rating...")

rating_type = pd.crosstab(
    df["rating"],
    df["type"]
)

rating_type.plot(
    kind="bar",
    figsize=(12, 6),
    colormap="Set2"
)

plt.title("Content Ratings by Content Type")
plt.xlabel("Content Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.legend(title="Content Type")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "type_vs_rating.png", dpi=300)
plt.close()


# ----------------------------------------------------------
# 4. COUNTRY VS CONTENT TYPE
# ----------------------------------------------------------

print("3. Analysing Country vs Content Type...")

country_data = df[["country", "type"]].copy()

country_data = country_data.dropna(subset=["country"])

country_data["country"] = country_data["country"].str.split(",")

country_data = country_data.explode("country")

# FIX: Reset index after explode
country_data = country_data.reset_index(drop=True)

country_data["country"] = country_data["country"].str.strip()

country_data = country_data[
    (country_data["country"] != "")
    & (country_data["country"] != "Unknown")
].copy()

# Identify top 10 countries
top_10 = country_data["country"].value_counts().head(10).index

country_top = country_data[
    country_data["country"].isin(top_10)
].copy()

# FIX: Reset index again before crosstab
country_top = country_top.reset_index(drop=True)

country_type = pd.crosstab(
    country_top["country"],
    country_top["type"]
)

country_type.plot(
    kind="bar",
    stacked=True,
    figsize=(12, 6),
    colormap="Set2"
)

plt.title("Movies and TV Shows by Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.legend(title="Content Type")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "country_vs_type.png", dpi=300)
plt.close()


# ----------------------------------------------------------
# 5. RELEASE YEAR VS MOVIE DURATION
# ----------------------------------------------------------

print("4. Analysing Release Year vs Movie Duration...")

movies = df[df["type"] == "Movie"].copy()

movies["release_decade"] = (
    movies["release_year"] // 10
) * 10

decade_duration = movies[
    (movies["release_year"] >= 1980)
    & (movies["duration_value"] > 0)
].copy()

plt.figure(figsize=(12, 6))

sns.boxplot(
    data=decade_duration,
    x="release_decade",
    y="duration_value",
    color="skyblue"
)

plt.title("Movie Duration Across Release Decades")
plt.xlabel("Release Decade")
plt.ylabel("Movie Duration (Minutes)")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "year_vs_movie_duration.png", dpi=300)
plt.close()


# ----------------------------------------------------------
# 6. RATING VS CONTENT TYPE HEATMAP
# ----------------------------------------------------------

print("5. Analysing Rating vs Content Type...")

rating_comparison = pd.crosstab(
    df["rating"],
    df["type"],
    normalize="columns"
) * 100

plt.figure(figsize=(10, 8))

sns.heatmap(
    rating_comparison,
    annot=True,
    fmt=".1f",
    cmap="YlGnBu",
    linewidths=0.5
)

plt.title("Content Rating Distribution by Type (%)")
plt.xlabel("Content Type")
plt.ylabel("Content Rating")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "rating_type_heatmap.png", dpi=300)
plt.close()


# ----------------------------------------------------------
# 7. DISPLAY RESULTS
# ----------------------------------------------------------

print("\n" + "=" * 55)
print("          BIVARIATE ANALYSIS RESULTS")
print("=" * 55)

print("\n1. Content Type vs Release Year:")
print(year_type.groupby("type")["count"].sum())

print("\n2. Content Type vs Content Rating:")
print(rating_type)

print("\n3. Country vs Content Type:")
print(country_type)

print("\n4. Movie Duration by Release Decade:")
print(
    decade_duration.groupby("release_decade")[
        "duration_value"
    ].agg(["count", "mean", "median"])
)

print("\n5. Rating vs Content Type (%):")
print(rating_comparison.round(2))

print("\n" + "=" * 55)
print("BIVARIATE ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 55)

print("\nAll five visualizations saved in:")
print(OUTPUT_DIR)
