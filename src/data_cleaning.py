"""Data loading and cleaning functions for the movie rating project."""

from pathlib import Path

import pandas as pd


def load_data(file_path: Path) -> pd.DataFrame:
    """Load the movie dataset from a CSV file."""
    return pd.read_csv(file_path)


def clean_movie_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean movie data and handle missing values in a beginner-friendly way."""
    cleaned = df.copy()

    cleaned["title"] = cleaned["title"].fillna("Unknown Title").str.strip()
    cleaned["genres"] = cleaned["genres"].fillna("Unknown")

    numeric_columns = ["release_year", "rating", "vote_count", "popularity"]
    for column in numeric_columns:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    cleaned["release_year"] = cleaned["release_year"].fillna(cleaned["release_year"].median()).astype(int)
    cleaned["rating"] = cleaned["rating"].fillna(cleaned["rating"].median())
    cleaned["vote_count"] = cleaned["vote_count"].fillna(0).astype(int)
    cleaned["popularity"] = cleaned["popularity"].fillna(cleaned["popularity"].median())

    cleaned = cleaned.drop_duplicates(subset=["movie_id", "title"])
    cleaned = cleaned[(cleaned["rating"] >= 0) & (cleaned["rating"] <= 5)]

    return cleaned.reset_index(drop=True)


def create_genre_table(df: pd.DataFrame) -> pd.DataFrame:
    """Split pipe-separated genres so each movie can appear once per genre."""
    genre_df = df.copy()
    genre_df["genre"] = genre_df["genres"].str.split("|")
    genre_df = genre_df.explode("genre")
    genre_df["genre"] = genre_df["genre"].str.strip()
    return genre_df
