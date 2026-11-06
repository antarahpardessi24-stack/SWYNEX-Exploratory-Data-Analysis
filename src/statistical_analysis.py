import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ----------------------------------------------------------
# 1. PROJECT CONFIGURATION
# ----------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = (
    PROJECT_ROOT / "data" / "processed" / "netflix_cleaned.csv"
)

REPORT_DIR = PROJECT_ROOT / "reports"
FIGURE_DIR = REPORT_DIR / "figures"

FIGURE_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)

sns.set_theme(style="whitegrid")

print("\nDataset loaded successfully!")
print("Dataset Shape:", df.shape)


# ----------------------------------------------------------
# 2. SEPARATE MOVIES AND TV SHOWS
# ----------------------------------------------------------

movies = df[df["type"] == "Movie"].copy()
tv_shows = df[df["type"] == "TV Show"].copy()

movie_duration = movies["duration_value"].dropna()
tv_seasons = tv_shows["duration_value"].dropna()

release_year = df["release_year"].dropna()


# ----------------------------------------------------------
# 3. DESCRIPTIVE STATISTICS
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("          DESCRIPTIVE STATISTICAL ANALYSIS")
print("=" * 60)

print("\nMOVIE DURATION STATISTICS (MINUTES)")
print(movie_duration.describe())

print("\nTV SHOW SEASON STATISTICS")
print(tv_seasons.describe())

print("\nRELEASE YEAR STATISTICS")
print(release_year.describe())


# ----------------------------------------------------------
# 4. CALCULATE CENTRAL TENDENCY
# ----------------------------------------------------------

def central_tendency(series):

    return {
        "Mean": series.mean(),
        "Median": series.median(),
        "Mode": series.mode().iloc[0],
    }


movie_central = central_tendency(movie_duration)
tv_central = central_tendency(tv_seasons)

print("\nMOVIE DURATION CENTRAL TENDENCY")
print(movie_central)

print("\nTV SHOW SEASON CENTRAL TENDENCY")
print(tv_central)


# ----------------------------------------------------------
# 5. CALCULATE DISPERSION
# ----------------------------------------------------------

def dispersion(series):

    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    return {
        "Variance": series.var(),
        "Standard Deviation": series.std(),
        "Minimum": series.min(),
        "Maximum": series.max(),
        "Q1": q1,
        "Q3": q3,
        "IQR": q3 - q1,
        "Skewness": series.skew(),
        "Kurtosis": series.kurt()
    }


movie_dispersion = dispersion(movie_duration)
tv_dispersion = dispersion(tv_seasons)

print("\nMOVIE DURATION DISPERSION")
print(movie_dispersion)

print("\nTV SHOW SEASON DISPERSION")
print(tv_dispersion)


# ----------------------------------------------------------
# 6. CREATE STATISTICAL SUMMARY TABLE
# ----------------------------------------------------------

summary = pd.DataFrame({
    "Movie Duration (Minutes)": {
        **movie_central,
        **movie_dispersion
    },
    "TV Show Seasons": {
        **tv_central,
        **tv_dispersion
    }
})

summary.to_csv(
    REPORT_DIR / "statistical_summary.csv"
)

print("\nSTATISTICAL SUMMARY TABLE")
print(summary.round(2))


# ----------------------------------------------------------
# 7. MOVIE DURATION DISTRIBUTION
# ----------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.histplot(
    movie_duration,
    bins=30,
    kde=True
)

plt.axvline(
    movie_duration.mean(),
    linestyle="--",
    label="Mean"
)

plt.axvline(
    movie_duration.median(),
    linestyle="-.",
    label="Median"
)

plt.title("Statistical Distribution of Movie Durations")
plt.xlabel("Movie Duration (Minutes)")
plt.ylabel("Number of Movies")
plt.legend()

plt.tight_layout()

plt.savefig(
    FIGURE_DIR / "statistical_movie_duration.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ----------------------------------------------------------
# 8. TV SHOW SEASON DISTRIBUTION
# ----------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.histplot(
    tv_seasons,
    discrete=True
)

plt.title("Statistical Distribution of TV Show Seasons")
plt.xlabel("Number of Seasons")
plt.ylabel("Number of TV Shows")

plt.tight_layout()

plt.savefig(
    FIGURE_DIR / "statistical_tv_seasons.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ----------------------------------------------------------
# 9. BOXPLOT FOR MOVIE DURATION
# ----------------------------------------------------------

plt.figure(figsize=(10, 5))

sns.boxplot(
    x=movie_duration,
    color="skyblue"
)

plt.title("Boxplot of Movie Durations")
plt.xlabel("Duration (Minutes)")

plt.tight_layout()

plt.savefig(
    FIGURE_DIR / "movie_duration_boxplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ----------------------------------------------------------
# 10. BOXPLOT FOR TV SHOW SEASONS
# ----------------------------------------------------------

plt.figure(figsize=(10, 5))

sns.boxplot(
    x=tv_seasons,
    color="lightgreen"
)

plt.title("Boxplot of TV Show Seasons")
plt.xlabel("Number of Seasons")

plt.tight_layout()

plt.savefig(
    FIGURE_DIR / "tv_seasons_boxplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ----------------------------------------------------------
# 11. CONTENT COUNTS BY TYPE
# ----------------------------------------------------------

content_counts = df["type"].value_counts()

print("\nCONTENT DISTRIBUTION")
print(content_counts)

print("\nMOVIE PERCENTAGE:")
print(round((len(movies) / len(df)) * 100, 2), "%")

print("\nTV SHOW PERCENTAGE:")
print(round((len(tv_shows) / len(df)) * 100, 2), "%")


# ----------------------------------------------------------
# 12. FINAL OUTPUT
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("       STATISTICAL ANALYSIS COMPLETED")
print("=" * 60)

print("\nFiles saved:")
print("1. reports/statistical_summary.csv")
print("2. reports/figures/statistical_movie_duration.png")
print("3. reports/figures/statistical_tv_seasons.png")
print("4. reports/figures/movie_duration_boxplot.png")
print("5. reports/figures/tv_seasons_boxplot.png")

print("\nAll statistical calculations completed successfully!")
