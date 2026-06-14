"""Run the complete Movie Rating Analysis workflow."""

from pathlib import Path

from analysis import (
    analyze_genres,
    analyze_voting_patterns,
    analyze_yearly_trends,
    calculate_summary_statistics,
    get_top_rated_movies,
)
from data_cleaning import clean_movie_data, create_genre_table, load_data
from reporting import write_summary_report
from visualization import create_all_visualizations


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "movies.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
FIGURES_DIR = OUTPUT_DIR / "figures"
REPORT_PATH = OUTPUT_DIR / "reports" / "summary_report.md"
CLEANED_DATA_PATH = OUTPUT_DIR / "cleaned_movies.csv"


def main() -> None:
    """Execute data cleaning, analysis, visualization, and reporting."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    raw_movies = load_data(DATA_PATH)
    cleaned_movies = clean_movie_data(raw_movies)
    genre_table = create_genre_table(cleaned_movies)

    summary_stats = calculate_summary_statistics(cleaned_movies)
    top_movies = get_top_rated_movies(cleaned_movies)
    genre_stats = analyze_genres(genre_table)
    yearly_stats = analyze_yearly_trends(cleaned_movies)
    voting_patterns = analyze_voting_patterns(cleaned_movies)

    cleaned_movies.to_csv(CLEANED_DATA_PATH, index=False)
    create_all_visualizations(cleaned_movies, top_movies, genre_stats, yearly_stats, FIGURES_DIR)
    write_summary_report(REPORT_PATH, summary_stats, top_movies, genre_stats, yearly_stats, voting_patterns)

    print("Movie Rating Analysis completed successfully.")
    print(f"Cleaned data saved to: {CLEANED_DATA_PATH}")
    print(f"Charts saved to: {FIGURES_DIR}")
    print(f"Summary report saved to: {REPORT_PATH}")


if __name__ == "__main__":
    main()
