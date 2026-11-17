# EraaSoft AI 805 — Lecture Tasks 24 to 28

Solutions to the EraaSoft AI 805 tasks for lectures 24–28. Each folder holds one lecture's deliverables.

| Lecture | Task | Folder | Deliverables |
|---|---|---|---|
| 24 | 28 Pandas Projects | [Lecture-24_Pandas-28-Projects](Lecture-24_Pandas-28-Projects) | 28 solved and executed notebooks + README |
| 25 | EDA: Video Game Sales, Netflix Shows | [Lecture-25_EDA](Lecture-25_EDA) | 2 notebooks + 2 reports |
| 26 | EDA: Facebook Metrics, IMDb, Telco Customer Churn | [Lecture-26_EDA](Lecture-26_EDA) | 3 notebooks + 3 reports |
| 27 | KPI reference guide across 9 business domains | [Lecture-27_KPIs](Lecture-27_KPIs) | PDF guide (40 KPIs) |
| 28 | 200 SQL practice questions | [Lecture-28_SQL](Lecture-28_SQL) | Answers with example queries |

## Lecture 25 — EDA
- `Task1_Video_Game_Sales_Analysis.ipynb` + `Task1_Report.md`: PS4 sales by game, genre, publisher, region and year.
- `Task2_Netflix_Shows_Analysis.ipynb` + `Task2_Report.md`: content mix, genres, countries, growth, ratings and durations.

## Lecture 26 — EDA
- `Task1_Facebook_Metrics_Analysis.ipynb` + report: post type, category, paid vs organic, timing and engagement metrics.
- `Task2_IMDb_Dataset_Analysis.ipynb` + report: title types, genres, runtimes, ratings, votes and trends. The raw IMDb files (title.basics, title.ratings) are too large for GitHub. Download them from <https://datasets.imdbws.com/> into `data/` and run `prepare_imdb.py` to rebuild `data/imdb_rated_movies.csv`. The prepared file is already included.
- `Task3_Telco_Customer_Churn_Analysis.ipynb` + report: churn by demographics, services, contract, payment, tenure and charges, with retention strategies.

## Data sources
Video Game Sales (Kaggle *sidtwr*, PS4 file), Netflix Shows (Kaggle *shivamb*, 2021 release), Facebook Metrics (UCI / Moro et al., 2016), IMDb non-commercial datasets, IBM Telco Customer Churn.

## Tools
Python, pandas, NumPy, Matplotlib, Seaborn, Jupyter.
