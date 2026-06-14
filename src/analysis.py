"""Analysis functions for movie ratings, genres, years, and voting patterns."""

import pandas as pd


def calculate_summary_statistics(df: pd.DataFrame) -> dict:
    """Calculate project-level summary statistics."""
    return {
        "total_movies": len(df),
        "average_rating": round(df["rating"].mean(), 2),
        "median_rating": round(df["rating"].median(), 2),
        "highest_rating": round(df["rating"].max(), 2),
        "lowest_rating": round(df["rating"].min(), 2),
        "average_vote_count": round(df["vote_count"].mean(), 2),
        "average_popularity": round(df["popularity"].mean(), 2),
        "earliest_year": int(df["release_year"].min()),
        "latest_year": int(df["release_year"].max()),
    }


def get_top_rated_movies(df: pd.DataFrame, min_votes: int = 500, limit: int = 10) -> pd.DataFrame:
    """Return top-rated movies with enough votes to avoid tiny-sample bias."""
    return (
        df[df["vote_count"] >= min_votes]
        .sort_values(["rating", "vote_count"], ascending=[False, False])
        .head(limit)
        [["title", "release_year", "rating", "vote_count", "popularity"]]
    )


def analyze_genres(genre_df: pd.DataFrame) -> pd.DataFrame:
    """Calculate average rating and activity by genre."""
    return (
        genre_df.groupby("genre")
        .agg(
            average_rating=("rating", "mean"),
            movie_count=("movie_id", "count"),
            average_popularity=("popularity", "mean"),
            total_votes=("vote_count", "sum"),
        )
        .reset_index()
        .sort_values("average_rating", ascending=False)
        .round({"average_rating": 2, "average_popularity": 2})
    )


def analyze_yearly_trends(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate yearly rating, popularity, and vote trends."""
    return (
        df.groupby("release_year")
        .agg(
            average_rating=("rating", "mean"),
            movie_count=("movie_id", "count"),
            average_popularity=("popularity", "mean"),
            total_votes=("vote_count", "sum"),
        )
        .reset_index()
        .sort_values("release_year")
        .round({"average_rating": 2, "average_popularity": 2})
    )


def analyze_voting_patterns(df: pd.DataFrame) -> dict:
    """Study how votes and popularity relate to ratings."""
    rating_vote_corr = df["rating"].corr(df["vote_count"])
    rating_popularity_corr = df["rating"].corr(df["popularity"])

    return {
        "rating_vote_correlation": round(rating_vote_corr, 2),
        "rating_popularity_correlation": round(rating_popularity_corr, 2),
        "most_voted_movie": df.sort_values("vote_count", ascending=False).iloc[0]["title"],
        "most_popular_movie": df.sort_values("popularity", ascending=False).iloc[0]["title"],
    }
