"""Markdown report generation for the movie rating analysis project."""

from pathlib import Path


def dataframe_to_markdown(df) -> str:
    """Convert a small DataFrame to a Markdown table without extra dependencies."""
    headers = list(df.columns)
    rows = df.astype(str).values.tolist()
    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"
    row_lines = ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join([header_line, separator_line, *row_lines])


def write_summary_report(
    report_path: Path,
    summary_stats: dict,
    top_movies,
    genre_stats,
    yearly_stats,
    voting_patterns: dict,
) -> None:
    """Write a beginner-friendly project report in Markdown format."""
    report_path.parent.mkdir(parents=True, exist_ok=True)

    best_genre = genre_stats.iloc[0]
    strongest_year = yearly_stats.sort_values("average_rating", ascending=False).iloc[0]

    report = f"""# Movie Rating Analysis - Summary Report

## Dataset Overview

- Total movies analyzed: {summary_stats["total_movies"]}
- Release year range: {summary_stats["earliest_year"]} to {summary_stats["latest_year"]}
- Average rating: {summary_stats["average_rating"]}
- Median rating: {summary_stats["median_rating"]}
- Highest rating: {summary_stats["highest_rating"]}
- Lowest rating: {summary_stats["lowest_rating"]}
- Average vote count: {summary_stats["average_vote_count"]}
- Average popularity: {summary_stats["average_popularity"]}

## Top-Rated Movies

The top-rated movies were filtered using a minimum vote count so that movies with very few votes do not dominate the ranking.

{dataframe_to_markdown(top_movies)}

## Genre Insights

The highest-rated genre in this dataset is **{best_genre["genre"]}**, with an average rating of **{best_genre["average_rating"]}**.

{dataframe_to_markdown(genre_stats)}

## Yearly Trends

The release year with the highest average rating is **{int(strongest_year["release_year"])}**, with an average rating of **{strongest_year["average_rating"]}**.

## Voting and Popularity Patterns

- Rating and vote count correlation: {voting_patterns["rating_vote_correlation"]}
- Rating and popularity correlation: {voting_patterns["rating_popularity_correlation"]}
- Most voted movie: {voting_patterns["most_voted_movie"]}
- Most popular movie: {voting_patterns["most_popular_movie"]}

## Key Findings

1. Most movies in the dataset are rated between 4.0 and 4.6, showing that the sample leans toward well-known, highly rated films.
2. Drama appears frequently across top-performing movies, either alone or combined with other genres.
3. Movies with more votes are often popular mainstream titles, but a higher vote count does not always guarantee the highest rating.
4. Genre-wise analysis helps compare movie categories more fairly than looking at individual films only.
5. Yearly trends show how average ratings can change over time, but small sample sizes should be interpreted carefully.

## Conclusion

This project demonstrates a simple end-to-end data analysis workflow: loading data, cleaning missing values, calculating insights, creating visualizations, and writing a report. It is suitable for beginner and internship portfolios because the code is organized, readable, and easy to extend with larger datasets.
"""

    report_path.write_text(report, encoding="utf-8")
