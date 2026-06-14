# Movie Rating Analysis - Summary Report

## Dataset Overview

- Total movies analyzed: 55
- Release year range: 1960 to 2023
- Average rating: 4.23
- Median rating: 4.2
- Highest rating: 4.8
- Lowest rating: 3.7
- Average vote count: 1674.49
- Average popularity: 79.05

## Top-Rated Movies

The top-rated movies were filtered using a minimum vote count so that movies with very few votes do not dominate the ranking.

| title | release_year | rating | vote_count | popularity |
| --- | --- | --- | --- | --- |
| The Shawshank Redemption | 1994 | 4.8 | 2345 | 92.1 |
| The Godfather | 1972 | 4.7 | 2101 | 89.3 |
| The Dark Knight | 2008 | 4.6 | 3250 | 96.4 |
| The Lord of the Rings: The Return of the King | 2003 | 4.6 | 3020 | 91.0 |
| Interstellar | 2014 | 4.6 | 2950 | 91.5 |
| Spirited Away | 2001 | 4.6 | 1250 | 79.1 |
| Inception | 2010 | 4.5 | 3100 | 94.8 |
| The Lord of the Rings: The Fellowship of the Ring | 2001 | 4.5 | 2888 | 88.9 |
| The Matrix | 1999 | 4.5 | 2605 | 90.2 |
| Oppenheimer | 2023 | 4.5 | 2300 | 92.9 |

## Genre Insights

The highest-rated genre in this dataset is **History**, with an average rating of **4.5**.

| genre | average_rating | movie_count | average_popularity | total_votes |
| --- | --- | --- | --- | --- |
| History | 4.5 | 1 | 92.9 | 2300 |
| Family | 4.45 | 2 | 78.45 | 2600 |
| Crime | 4.32 | 13 | 82.24 | 23519 |
| Drama | 4.28 | 36 | 80.0 | 61212 |
| Biography | 4.28 | 4 | 81.35 | 6672 |
| Fantasy | 4.26 | 5 | 88.66 | 12423 |
| Music | 4.25 | 2 | 73.4 | 2180 |
| Thriller | 4.25 | 6 | 79.12 | 9600 |
| Animation | 4.24 | 7 | 77.71 | 9690 |
| Mystery | 4.23 | 3 | 77.87 | 4333 |
| Sci-Fi | 4.22 | 10 | 81.84 | 19925 |
| Adventure | 4.22 | 20 | 84.27 | 40193 |
| Documentary | 4.2 | 1 | 45.6 | 180 |
| Action | 4.19 | 13 | 88.68 | 29850 |
| Unknown | 4.1 | 1 | 42.5 | 0 |
| Comedy | 4.07 | 10 | 77.75 | 14190 |
| Romance | 4.03 | 3 | 84.42 | 5187 |
| Horror | 3.95 | 2 | 75.55 | 2450 |

## Yearly Trends

The release year with the highest average rating is **1972**, with an average rating of **4.7**.

## Voting and Popularity Patterns

- Rating and vote count correlation: 0.41
- Rating and popularity correlation: 0.33
- Most voted movie: The Avengers
- Most popular movie: The Dark Knight

## Key Findings

1. Most movies in the dataset are rated between 4.0 and 4.6, showing that the sample leans toward well-known, highly rated films.
2. Drama appears frequently across top-performing movies, either alone or combined with other genres.
3. Movies with more votes are often popular mainstream titles, but a higher vote count does not always guarantee the highest rating.
4. Genre-wise analysis helps compare movie categories more fairly than looking at individual films only.
5. Yearly trends show how average ratings can change over time, but small sample sizes should be interpreted carefully.

## Conclusion

This project demonstrates a simple end-to-end data analysis workflow: loading data, cleaning missing values, calculating insights, creating visualizations, and writing a report. It is suitable for beginner and internship portfolios because the code is organized, readable, and easy to extend with larger datasets.
