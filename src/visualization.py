"""Visualization functions using Matplotlib and Seaborn."""

from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


def setup_style() -> None:
    """Apply a clean chart style."""
    sns.set_theme(style="whitegrid", palette="Set2")
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.rcParams["axes.titlesize"] = 14
    plt.rcParams["axes.labelsize"] = 11


def save_rating_distribution(df, output_dir: Path) -> None:
    """Create a histogram showing how ratings are distributed."""
    plt.figure()
    sns.histplot(df["rating"], bins=10, kde=True)
    plt.title("Movie Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")
    plt.tight_layout()
    plt.savefig(output_dir / "rating_distribution.png", dpi=150)
    plt.close()


def save_top_rated_movies(top_movies, output_dir: Path) -> None:
    """Create a bar chart of the top-rated movies."""
    plt.figure(figsize=(11, 7))
    sns.barplot(data=top_movies, x="rating", y="title", hue="title", legend=False)
    plt.title("Top-Rated Movies")
    plt.xlabel("Average Rating")
    plt.ylabel("Movie")
    plt.xlim(3.5, 5.0)
    plt.tight_layout()
    plt.savefig(output_dir / "top_rated_movies.png", dpi=150)
    plt.close()


def save_genre_wise_ratings(genre_stats, output_dir: Path) -> None:
    """Create a chart comparing average ratings by genre."""
    chart_data = genre_stats.sort_values("average_rating", ascending=False)

    plt.figure(figsize=(11, 7))
    sns.barplot(data=chart_data, x="average_rating", y="genre", hue="genre", legend=False)
    plt.title("Average Rating by Genre")
    plt.xlabel("Average Rating")
    plt.ylabel("Genre")
    plt.xlim(3.5, 5.0)
    plt.tight_layout()
    plt.savefig(output_dir / "genre_wise_ratings.png", dpi=150)
    plt.close()


def save_yearly_trends(yearly_stats, output_dir: Path) -> None:
    """Create a line chart for rating trends over release years."""
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=yearly_stats, x="release_year", y="average_rating", marker="o")
    plt.title("Average Movie Rating by Release Year")
    plt.xlabel("Release Year")
    plt.ylabel("Average Rating")
    plt.ylim(3.5, 5.0)
    plt.tight_layout()
    plt.savefig(output_dir / "yearly_rating_trends.png", dpi=150)
    plt.close()


def save_vote_count_vs_rating(df, output_dir: Path) -> None:
    """Create a scatter plot showing vote count and rating relationship."""
    plt.figure()
    sns.scatterplot(data=df, x="vote_count", y="rating", size="popularity", hue="popularity", sizes=(40, 250))
    plt.title("Vote Count vs Rating")
    plt.xlabel("Vote Count")
    plt.ylabel("Rating")
    plt.tight_layout()
    plt.savefig(output_dir / "vote_count_vs_rating.png", dpi=150)
    plt.close()


def create_all_visualizations(df, top_movies, genre_stats, yearly_stats, output_dir: Path) -> None:
    """Generate every chart used in the project."""
    setup_style()
    output_dir.mkdir(parents=True, exist_ok=True)

    save_rating_distribution(df, output_dir)
    save_top_rated_movies(top_movies, output_dir)
    save_genre_wise_ratings(genre_stats, output_dir)
    save_yearly_trends(yearly_stats, output_dir)
    save_vote_count_vs_rating(df, output_dir)
