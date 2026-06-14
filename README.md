# Intern Details

- **Intern ID:** CITS1623
- **Full Name:** JONNA ABHISHEK
- **Duration:** 4 Weeks

# Movie Rating Analysis

An intermediate-level, internship-friendly Python data analysis project that studies movie ratings, genres, release years, popularity, and voting patterns using a MovieLens-style ratings dataset.

## Project Goals

- Clean and prepare movie rating data.
- Handle missing values in movie metadata and ratings.
- Analyze rating distributions, top-rated movies, genre performance, yearly trends, and voting behavior.
- Create clear visualizations using Matplotlib and Seaborn.
- Generate a simple summary report that explains the main findings.

## Dataset

This project includes a small sample dataset in `data/movies.csv`. The columns are:

- `movie_id`: Unique movie identifier
- `title`: Movie name
- `genres`: Pipe-separated genre labels
- `release_year`: Year the movie was released
- `rating`: Average user rating from 0 to 5
- `vote_count`: Number of ratings/votes
- `popularity`: Popularity score

You can replace `data/movies.csv` with a larger IMDb, TMDb, or MovieLens dataset as long as it contains similar columns.

## Folder Structure

```text
Movie_Rating_Analysis/
├── data/
│   └── movies.csv
├── outputs/
│   ├── figures/
│   └── reports/
├── src/
│   ├── analysis.py
│   ├── data_cleaning.py
│   ├── reporting.py
│   ├── visualization.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the full analysis:

```bash
python src/main.py
```

## Outputs

Running the project creates:

- Cleaned dataset: `outputs/cleaned_movies.csv`
- Summary report: `outputs/reports/summary_report.md`
- Visualizations:
  - `outputs/figures/rating_distribution.png`
  - `outputs/figures/top_rated_movies.png`
  - `outputs/figures/genre_wise_ratings.png`
  - `outputs/figures/yearly_rating_trends.png`
  - `outputs/figures/vote_count_vs_rating.png`

## Key Questions Answered

- What is the overall rating distribution?
- Which movies are top-rated after considering vote count?
- Which genres have the highest average ratings?
- How have movie ratings changed over time?
- Are popular or frequently voted movies rated differently?

## Skills Demonstrated

- Python project organization
- Pandas data cleaning
- Missing value handling
- Exploratory data analysis
- Matplotlib and Seaborn visualizations
- Markdown report generation

## Notes for Beginners

The project is intentionally simple and readable. Each source file focuses on one responsibility:

- `data_cleaning.py` prepares the data.
- `analysis.py` calculates statistics and insights.
- `visualization.py` creates charts.
- `reporting.py` writes the findings report.
- `main.py` runs everything in order.
